#!/usr/bin/env python3
"""
Comprehensive test runner for all EvoAI Commerce Agent tests.
"""
import subprocess
import sys
from pathlib import Path

def run_command(cmd: list, description: str) -> bool:
    """Run a command and return success status."""
    print(f"\n{'='*60}")
    print(f"Running: {description}")
    print(f"{'='*60}")
    
    try:
        result = subprocess.run(cmd, check=True, capture_output=False)
        print(f"✓ {description} completed successfully")
        return True
    except subprocess.CalledProcessError as e:
        print(f"✗ {description} failed with exit code {e.returncode}")
        return False
    except Exception as e:
        print(f"✗ {description} failed with error: {e}")
        return False

def main():
    """Run all test suites."""
    print("EvoAI Commerce Agent - Comprehensive Test Suite")
    
    tests = [
        {
            "cmd": [sys.executable, "tests/test_policy.py"],
            "description": "60-minute policy unit tests"
        },
        {
            "cmd": [sys.executable, "tests/test_schema.py"], 
            "description": "JSON schema validation tests"
        },
        {
            "cmd": [sys.executable, "tests/run_tests_mock.py"],
            "description": "Main integration tests (4 required scenarios)"
        }
    ]
    
    results = []
    
    for test in tests:
        success = run_command(test["cmd"], test["description"])
        results.append((test["description"], success))
    
    # Summary
    print(f"\n{'='*60}")
    print("TEST SUMMARY")
    print(f"{'='*60}")
    
    all_passed = True
    for description, success in results:
        status = "✓ PASS" if success else "✗ FAIL"
        print(f"{status}: {description}")
        if not success:
            all_passed = False
    
    print(f"\n{'='*60}")
    if all_passed:
        print("🎉 ALL TESTS PASSED!")
        print("Your EvoAI Commerce Agent is ready for submission.")
    else:
        print("❌ SOME TESTS FAILED")
        print("Please fix the failing tests before submission.")
        sys.exit(1)
    print(f"{'='*60}")

if __name__ == "__main__":
    main()