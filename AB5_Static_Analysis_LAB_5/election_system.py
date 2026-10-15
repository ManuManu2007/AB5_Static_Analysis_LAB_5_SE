"""Voting and election management system."""

import secrets
from datetime import datetime

from defusedxml import ElementTree
from defusedxml.common import DefusedXmlException


POLLS_CLOSE_HOUR = 18

voters = {}
ballots = []
candidates = ["Alice", "Bob", "NOTA"]


def register_voter(voter_id, name, age):
    """Register an eligible voter."""
    if age < 18 or voter_id in voters:
        return False

    voters[voter_id] = {
        "name": name,
        "voted": False,
    }
    return True


def is_officer(role):
    """Check whether a user has the election officer role."""
    return role == "election_officer"


def cast_vote(voter_id, candidate, when):
    """Record a valid vote before the polls close."""
    if voter_id not in voters:
        return False

    if voters[voter_id]["voted"]:
        return False

    if candidate not in candidates:
        return False

    if when.hour >= POLLS_CLOSE_HOUR:
        return False

    ballots.append(candidate)
    voters[voter_id]["voted"] = True
    return True


def tally():
    """Count votes for each candidate."""
    counts = {}

    for ballot in ballots:
        counts[ballot] = counts.get(ballot, 0) + 1

    return counts


def winner():
    """Return the candidate with the most votes, or None."""
    counts = tally()

    if not counts:
        return None

    return max(counts, key=counts.get)


def vote_percent(name):
    """Calculate a candidate's percentage of all ballots."""
    total = len(ballots)

    if total == 0:
        return 0.0

    return tally().get(name, 0) * 100 / total


def turnout():
    """Calculate the percentage of registered voters who voted."""
    if not voters:
        return 0.0

    votes_cast = sum(
        voter["voted"] for voter in voters.values()
    )

    return votes_cast * 100 / len(voters)


def count_for(candidate, ballot_list):
    """Count ballots belonging to a specified candidate."""
    return sum(
        ballot == candidate for ballot in ballot_list
    )


def announce():
    """Return the vote count for every candidate."""
    counts = tally()

    return [
        f"{name}: {counts.get(name, 0)}"
        for name in candidates
    ]


def receipt_number():
    """Generate a receipt number using a secure random generator."""
    return f"RCPT-{secrets.randbelow(900000) + 100000}"


def import_postal_ballots(xml_text):
    """Import valid postal ballots from XML."""
    try:
        root = ElementTree.fromstring(xml_text)
    except (ElementTree.ParseError, DefusedXmlException):
        return 0

    imported = 0

    for node in root.iter("ballot"):
        candidate = node.get("candidate")
        voter_id = node.get("voter")

        if candidate not in candidates:
            continue

        if voter_id not in voters:
            continue

        if voters[voter_id]["voted"]:
            continue

        ballots.append(candidate)
        voters[voter_id]["voted"] = True
        imported += 1

    return imported


def main():
    """Run sample election operations."""
    print(
        "Register Asha (age 18):",
        register_voter("V1", "Asha", 18),
    )

    register_voter("V2", "Ben", 30)
    register_voter("V3", "Chen", 45)
    register_voter("V4", "Dia", 22)

    print(
        "Is a plain 'voter' an election officer?",
        is_officer("voter"),
    )

    print(
        "Ben votes Alice:",
        cast_vote(
            "V2", "Alice", datetime(2026, 11, 20, 10, 0)
        ),
    )

    print(
        "Ben votes Alice again:",
        cast_vote(
            "V2", "Alice", datetime(2026, 11, 20, 11, 0)
        ),
    )

    print(
        "Chen votes 'bob':",
        cast_vote(
            "V3", "bob", datetime(2026, 11, 20, 12, 0)
        ),
    )

    print(
        "Dia votes Bob at 18:30:",
        cast_vote(
            "V4", "Bob", datetime(2026, 11, 20, 18, 30)
        ),
    )

    postal_xml = (
        "<postal>"
        "<ballot voter='V1' candidate='Bob'/>"
        "</postal>"
    )

    print(
        "Postal ballots imported:",
        import_postal_ballots(postal_xml),
    )

    print("Tally:", tally())
    print("Winner:", winner())
    print("Alice %:", vote_percent("Alice"))
    print("Turnout %:", turnout())
    print("Announcements:", announce())
    print("Receipt:", receipt_number())


if __name__ == "__main__":
    main()
