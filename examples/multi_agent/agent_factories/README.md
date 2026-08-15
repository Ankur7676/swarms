# Agent Factories

This directory demonstrates building reusable agent factory functions and composing them into a collaborative multi-agent workflow.

## Examples

- [agent_factories.py](agent_factories.py) - Factory functions (`build_researcher_agent`, `build_coder_agent`, `build_reviewer_agent`) that each return a fresh `Agent` instance
- [workflow_example.py](workflow_example.py) - Chains the three factory-built agents into a `SequentialWorkflow` (research → code → review)

## Overview

Factory functions are useful when you need multiple independent instances of the same agent role (e.g. one team per request) without agents sharing `agent_name` — and therefore colliding on `persistent_memory`. Call a factory each time you need a new instance rather than reusing a single module-level `Agent`.
