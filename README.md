# Should We Go to This Event?

A tiny Python tool that helps evaluate whether an event is worth attending based on audience fit, lead potential, cost, travel, and strategic value.

## Why I built this

I like building small, lightweight tools to test ideas and turn decision-making into something more structured. This project is based on a real question event teams face: how do you quickly evaluate whether an event is worth the investment?

## What it does

The script asks for:
- audience fit
- estimated leads
- total cost
- travel requirements
- strategic value

It then returns:
- a recommendation (Go / Maybe / Skip)
- a score
- a short explanation of the reasoning

## How to run it

```bash
python3 event_decider.py
