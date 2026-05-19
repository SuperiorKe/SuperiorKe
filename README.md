# Kenn Macharia

> I build operational infrastructure for the informal economy — tools that help the people running African commerce and civic life run like professionals.

Backend engineer in Nairobi. Founder of [SuperiaTech](https://superiatech.vercel.app/). I work in Python and Node.js on cloud, on systems that have to survive USSD sessions, M-Pesa callbacks, Swahili-English code-switching, and users who will never download an app.

That constraint is the work.

---

## Selected work

### Sauti ya Mwananchi — civic-accountability AI agent
*Cite-or-refuse Gemini middleware on Cloud Run*

Answers Kenyan voters' civic questions in English, Swahili, or Sheng — grounded in the Constitution of Kenya 2010 and the IEBC Voter Guide. A custom Python middleware intercepts every model response and rejects anything without a primary-source citation. The model never reaches the user unchecked.

**Stack:** Python · FastAPI · Google ADK · Gemini 2.0 (Vertex AI) · Cloud Run · Playwright
[Live](https://sauti-ya-mwananchi-mu44pr45ha-uc.a.run.app) · [GitHub](https://github.com/SuperiorKe/sauti-ya-mwananchi)

---

### Afrimall — production e-commerce platform
*Full-stack commerce shipped end-to-end for a US client*

Next.js 15 + Payload CMS storefront, admin, and API in one app. PostgreSQL, Stripe checkout with webhook reconciliation, transactional email, deployed on Vercel. Real customers, real transactions.

**Stack:** Next.js 15 · TypeScript · Payload CMS · PostgreSQL · Stripe · Vercel
[Live](https://afrimall.app) · [GitHub](https://github.com/SuperiorKe/afrimall)

---

### Agent Governance Platform — zero-trust HITL infrastructure
*Rule engine, audit log, and Socket.io approvals for AI agents*

An infrastructure layer between AI agents and the systems they act on. Agents submit proposed actions; a deterministic rule engine auto-approves, blocks, or routes to a human via a real-time dashboard. Every decision is audited. NPM monorepo, Express + Knex + SQLite + Socket.io, lifecycle sweep workers.

**Stack:** Node.js · Express · Knex · SQLite · Socket.io · React · Vite
[GitHub](https://github.com/SuperiorKe/AgentGovernance)

---

### ParkaSmart — parking ops for African malls
*Replaces handwritten ledger books with USSD/SMS*

Replaces handwritten parking ledger books in commercial properties. Real-time vehicle logging, automated payment tracking, end-of-day SMS reports to managers. Built for the Africa's Talking Real Estate Hackathon 2026.

**Stack:** Next.js 16 · TypeScript · Drizzle ORM · SQLite · Africa's Talking (SMS/USSD/Airtime)
[GitHub](https://github.com/SuperiorKe/ParkaSmart)

---

### RentPay — USSD rent collection
*M-Pesa STK Push and SMS invoicing on feature phones*

USSD-based rent payment for Kenyan landlords. Tenants pay rent over a basic phone via M-Pesa STK Push; landlords send invoices and track payments through a Flask dashboard. No app, no data plan required.

**Stack:** Python · Flask · M-Pesa Daraja API · Africa's Talking · SQLite
[GitHub](https://github.com/SuperiorKe/RentPay)

---

### Eliana Textiles — Nairobi SMB storefront
*Luxury bedding storefront with serverless backend and full test coverage*

Storefront for a Nairobi-based bedding brand at OTC Wholesale Mall. React 19 + Vite + Vercel serverless functions, with Playwright E2E and Vitest unit tests covering the catalog and checkout flows.

**Stack:** React 19 · TypeScript · Vite · Tailwind 4 · Vercel serverless · Playwright · Vitest
[Live](https://eliana-textiles.vercel.app) · [GitHub](https://github.com/SuperiorKe/eliana-textiles)

---

## Stack

```
Languages       Python · TypeScript · JavaScript · SQL
Backend         FastAPI · Flask · Express · Next.js (App Router) · Payload CMS
Frontend        React · Next.js · Tailwind
Data            PostgreSQL · SQLite · Drizzle · Knex
Cloud           AWS · Google Cloud (Cloud Run, Vertex AI) · Vercel
Infrastructure  Docker · GitHub Actions
Telco / Mobile  Africa's Talking (SMS/USSD/Airtime) · M-Pesa Daraja
AI              Gemini · LangChain · Google ADK
```

---

## Certifications

- **AWS Certified Cloud Practitioner** — Oct 2024
- **AWS Academy Graduate, Cloud Foundations** — Dec 2024
- **Africa's Talking × Google AI Program** — Oct 2025
- **Kubernetes and Cloud Native Associate (KCNA)** — in progress

---

## What I'm looking for

A backend engineering role — Node.js, Python, or cloud-leaning — on a team that ships to real users in environments where reliability matters more than novelty. I work best alongside engineers who care about the system surviving Monday morning, not just Friday's demo.

---

## Contact

- superiorwech@gmail.com
- [LinkedIn](https://linkedin.com/in/kenn-macharia)
- [SuperiaTech](https://superiatech.vercel.app/)
- Nairobi, Kenya · open to remote

---

*The best technology disappears into the background and helps people get their work done better.*
