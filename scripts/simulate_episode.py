#!/usr/bin/env python3
"""Minimal prototype for King AI Empire highlight detection.

Runs a toy match simulation and prints when the recorder should
switch from timelapse to realtime due to significant events.
"""

from __future__ import annotations

from dataclasses import dataclass
from random import Random


@dataclass
class TeamState:
    name: str
    base_hp: int = 10_000
    tech_tier: int = 0
    units_alive: int = 10


def significance_score(
    dps_spike: float,
    tech_unlock: float,
    streak_kill: float,
    base_hp_drop: float,
    frontline_shift: float,
    underdog_comeback: float,
) -> float:
    return (
        dps_spike * 0.24
        + tech_unlock * 0.18
        + streak_kill * 0.15
        + base_hp_drop * 0.23
        + frontline_shift * 0.12
        + underdog_comeback * 0.08
    )


def simulate(seed: int = 7, steps: int = 180) -> None:
    rng = Random(seed)
    team_dark = TeamState(name="Obsidian Legion")
    team_light = TeamState(name="Aether Dominion")

    trigger = 0.52
    recorder_mode = "timelapse"

    print("== King AI Empire match simulation ==")
    transitions = 0
    for t in range(1, steps + 1):
        attacker, defender = (
            (team_dark, team_light) if rng.random() < 0.5 else (team_light, team_dark)
        )

        damage = rng.randint(12, 120)
        defender.base_hp = max(0, defender.base_hp - damage)

        tech_unlock = 0.0
        if attacker.tech_tier < 3 and rng.random() < 0.02:
            attacker.tech_tier += 1
            tech_unlock = 1.0

        score = significance_score(
            dps_spike=min(1.0, damage / 120.0),
            tech_unlock=tech_unlock,
            streak_kill=rng.random() * 0.9,
            base_hp_drop=min(1.0, damage / 200.0),
            frontline_shift=rng.random(),
            underdog_comeback=rng.random() * 0.7,
        )

        new_mode = "realtime" if score >= trigger else "timelapse"
        if new_mode != recorder_mode:
            recorder_mode = new_mode
            transitions += 1
            print(
                f"t={t:03d}s | MODE -> {recorder_mode.upper()} | score={score:.2f} | "
                f"{team_dark.name} HP={team_dark.base_hp} | {team_light.name} HP={team_light.base_hp}"
            )

        if team_dark.base_hp == 0 or team_light.base_hp == 0:
            winner = team_light.name if team_dark.base_hp == 0 else team_dark.name
            print(f"t={t:03d}s | WINNER: {winner}")
            print(f"Transitions detected: {transitions}")
            break
    else:
        print(
            f"END t={steps}s | {team_dark.name} HP={team_dark.base_hp} | "
            f"{team_light.name} HP={team_light.base_hp} | Transitions detected: {transitions}"
        )


if __name__ == "__main__":
    simulate()
