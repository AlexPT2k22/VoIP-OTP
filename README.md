# VoIP OTP — FastAPI microservice for OTP authentication via SMS and voice calls using Twilio and Redis

[![wakatime](https://wakatime.com/badge/user/018b251f-0e34-47a2-be9d-82c5e052e073/project/dd33194c-697b-4583-9fdb-d0a78a4e3aed.svg)](https://wakatime.com/badge/user/018b251f-0e34-47a2-be9d-82c5e052e073/project/dd33194c-697b-4583-9fdb-d0a78a4e3aed)
[![CI](https://github.com/AlexPT2k22/voip-otp/actions/workflows/ci.yml/badge.svg)](https://github.com/AlexPT2k22/voip-otp/actions/workflows/ci.yml)
[![Python](https://img.shields.io/badge/python-3.9+-blue.svg)](https://python.org)
[![License](https://img.shields.io/badge/license-MIT-green.svg)](LICENSE)

FastAPI microservice for OTP authentication via SMS and voice calls,
powered by Twilio and Redis.

## Features
- OTP delivery via SMS and voice calls (Twilio)
- HMAC-SHA256 OTP hashing — time-safe comparison
- Sliding window rate limiting per phone number (Redis sorted sets)
- Resend cooldown and max verification attempts
- Docker + docker-compose for local development
- Fully async
- CI/CD pipeline with linting, type checking, testing, and security scans
## Tech Stack
| Layer          | Technology                        |
| -------------- | --------------------------------- |
| Framework      | FastAPI                           |
| Cache / Store  | Redis                             |
| Notifications | Twilio (SMS + Voice)              |
| Validation     | Pydantic v2 + pydantic-settings   |
| Testing        | pytest + pytest-asyncio + fakeredis|
| Linting        | ruff + mypy (strict)              |
| CI/CD          | GitHub Actions                    |
| Container      | Docker + docker-compose           |
