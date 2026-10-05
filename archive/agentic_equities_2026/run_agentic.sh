#!/bin/bash
cd /root/lifecoach/island-fund-repo
cat agentic_equities/prompt.md | claude --print >> agentic_equities/cron.log 2>&1
