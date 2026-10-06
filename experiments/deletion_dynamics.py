#!/usr/bin/env python3
"""Exhaustive tools for local-extrema deletion dynamics.

Base rule: in a current sequence of distinct values, delete an interior term
that lies strictly between its two current neighbours.
"""

from __future__ import annotations

import argparse
import itertools
from collections import Counter
from functools import lru_cache
from math import factorial
from typing import Iterable, Sequence, Tuple

State = Tuple[Tuple[int, int], ...]  # (original_index, value)


def between(a: int, b: int, c: int) -> bool:
    return (a < b < c) or (a > b > c)


def legal_positions(state: State) -> tuple[int, ...]:
    return tuple(
        i
        for i in range(1, len(state) - 1)
        if between(state[i - 1][1], state[i][1], state[i + 1][1])
    )


def delete_at(state: State, i: int) -> State:
    return state[:i] + state[i + 1 :]


def labelled(values: Sequence[int]) -> State:
    return tuple(enumerate(values))


def core_indices(values: Sequence[int]) -> tuple[int, ...]:
    n = len(values)
    if n == 0:
        return ()
    if n == 1:
        return (0,)
    core = [0]
    for i in range(1, n - 1):
        a, b, c = values[i - 1], values[i], values[i + 1]
        if (a < b > c) or (a > b < c):
            core.append(i)
    core.append(n - 1)
    return tuple(core)


def survivor_count(values: Sequence[int]) -> int:
    return len(core_indices(values))


@lru_cache(maxsize=None)
def terminal_index_sets(state: State) -> frozenset[tuple[int, ...]]:
    legal = legal_positions(state)
    if not legal:
        return frozenset({tuple(i for i, _ in state)})
    out = set()
    for i in legal:
        out.update(terminal_index_sets(delete_at(state, i)))
    return frozenset(out)


@lru_cache(maxsize=None)
def reachable_states(state: State) -> frozenset[State]:
    out = {state}
    for i in legal_positions(state):
        out.update(reachable_states(delete_at(state, i)))
    return frozenset(out)


def verify_permutation(p: Sequence[int]) -> None:
    state = labelled(p)
    core = core_indices(p)
    d = len(p) - len(core)

    terminals = terminal_index_sets(state)
    assert terminals == frozenset({core}), (p, terminals, core)

    states = reachable_states(state)
    assert len(states) == 2**d, (p, len(states), d)

    core_set = set(core)
    for s in states:
        present = {i for i, _ in s}
        assert core_set <= present

        # Every remaining non-core term must still be legal.
        legal_original_indices = {s[i][0] for i in legal_positions(s)}
        assert present - core_set == legal_original_indices, (
            p,
            s,
            present - core_set,
            legal_original_indices,
        )


def verify_up_to(nmax: int) -> None:
    total = 0
    for n in range(1, nmax + 1):
        count = 0
        for p in itertools.permutations(range(1, n + 1)):
            verify_permutation(p)
            count += 1
        total += count
        print(f"n={n}: verified {count} permutations")
    print(f"total verified: {total}")


def distribution(n: int) -> Counter[int]:
    out: Counter[int] = Counter()
    for p in itertools.permutations(range(1, n + 1)):
        out[survivor_count(p)] += 1
    return out


def print_distribution(n: int) -> None:
    dist = distribution(n)
    print(f"survivor distribution for n={n}")
    for k in sorted(dist):
        d = n - k
        print(
            f"k={k}: permutations={dist[k]}, "
            f"reachable_states={2**d} per permutation with this k, "
            f"complete_histories={factorial(d)}"
        )


def main() -> None:
    parser = argparse.ArgumentParser()
    sub = parser.add_subparsers(dest="cmd", required=True)

    verify = sub.add_parser("verify", help="exhaustively verify the base theorems")
    verify.add_argument("--nmax", type=int, default=8)

    dist = sub.add_parser("distribution", help="count permutations by survivors")
    dist.add_argument("n", type=int)

    args = parser.parse_args()

    if args.cmd == "verify":
        verify_up_to(args.nmax)
    elif args.cmd == "distribution":
        print_distribution(args.n)


if __name__ == "__main__":
    main()
