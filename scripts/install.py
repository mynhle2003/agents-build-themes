#!/usr/bin/env python3
"""Install completed skill folders without replacing existing local content."""
import argparse
import hashlib
import shutil
from pathlib import Path


def fingerprint(folder):
    if folder.is_symlink() or not folder.is_dir():
        return None
    result = {}
    for path in sorted(folder.rglob('*')):
        if path.is_symlink():
            return None
        if path.is_file():
            result[str(path.relative_to(folder))] = hashlib.sha256(path.read_bytes()).hexdigest()
    return result


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('repo', type=Path)
    parser.add_argument('--group', choices=['build', 'qa', 'setup-store'])
    parser.add_argument('--dry-run', action='store_true')
    args = parser.parse_args()
    repo = args.repo.expanduser().resolve()
    if not repo.is_dir():
        parser.error('Repo destination must already exist.')
    package = Path(__file__).resolve().parents[1]
    if repo == package or package in repo.parents:
        parser.error('Choose a theme repo outside this skill package.')
    source = package / 'skills'
    if args.group:
        source /= args.group
    entries = sorted(source.rglob('SKILL.md'))
    if not entries:
        parser.error('No completed skills found.')
    destination = repo / '.agents' / 'skills'
    if (repo / '.agents').is_symlink() or destination.is_symlink():
        parser.error('Destination .agents and skills must be real directories.')
    pending = []
    conflicts = []
    names = set()
    for entry in entries:
        skill = entry.parent
        if skill.name in names:
            parser.error('Duplicate skill directory name: ' + skill.name)
        names.add(skill.name)
        target = destination / skill.name
        if target.exists() or target.is_symlink():
            if fingerprint(skill) == fingerprint(target):
                print('UNCHANGED ' + str(target))
            else:
                conflicts.append(target)
        else:
            pending.append((skill, target))
    if conflicts:
        for target in conflicts:
            print('CONFLICT ' + str(target))
        parser.exit(1, 'No skill copied. Review existing skills before installing.\n')
    for skill, target in pending:
        print(('WOULD COPY ' if args.dry_run else 'COPY ') + str(target))
    if not args.dry_run:
        destination.mkdir(parents=True, exist_ok=True)
        for skill, target in pending:
            shutil.copytree(skill, target)


if __name__ == '__main__':
    main()
