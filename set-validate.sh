#!/bin/bash

echo "🔍 SET Local Validation"
echo "-----------------------"

# Check files
if [ ! -f "SET-POLICY.json" ]; then
  echo "❌ Missing SET-POLICY.json"
  exit 1
fi

if [ ! -f "SET-CLAIM.json" ]; then
  echo "❌ Missing SET-CLAIM.json"
  exit 1
fi

# Extract values
CLAIM_STATUS=$(jq -r '.status' SET-CLAIM.json)
CLAIM_VERSION=$(jq -r '.version' SET-CLAIM.json)
REQUIRED_VERSION=$(jq -r '.execution_policy.require_version' SET-POLICY.json)

# Validate status
if [ "$CLAIM_STATUS" != "compliant" ]; then
  echo "❌ Status is not compliant"
  exit 1
fi

# Validate version
if [ "$CLAIM_VERSION" != "$REQUIRED_VERSION" ]; then
  echo "❌ Version mismatch"
  exit 1
fi

echo "✅ Policy satisfied locally"
