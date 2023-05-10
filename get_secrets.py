#!/usr/bin/env python3

import subprocess

def read(op_url):
    assert op_url.startswith("op://")
    r = subprocess.run(['op', 'read', '--no-newline', op_url], check=True, capture_output=True, universal_newlines=True)
    return r.stdout

def read_recursive(v: dict|str) -> str|dict:
    if isinstance(v, str):
        return read(v)
    return {k: read_recursive(v) for k, v in v.items()}

if __name__ == '__main__':
    import json
    import sys

    query: dict[str, str] = json.loads(json.load(sys.stdin)["q"])
    assert isinstance(query, dict)

    json.dump({"o": json.dumps(read_recursive(query))}, sys.stdout)
