# Algorithmic Trading System & Task Automation Bot

An adaptive, Python-based algorithmic trading system focused on dynamic risk management, multi-timeframe data analysis, and self-tuning optimization. Developed iteratively as a complex system engineering project, this bot transitions from static rule-based execution to an adaptive, data-driven architecture.

## Core Features & Architecture

* **Dynamic Risk Management (Edge-Based Sizing):** Adjusts position sizes dynamically based on setup probability and market volatility, rather than fixed-lot trading. Includes a "Kill Switch" mechanism for daily loss limits.
* **Multi-Timeframe (MTF) Analysis:** Evaluates market conditions across multiple timeframes simultaneously to prevent false signals and align with macro trends.
* **Walk-Forward Optimization (Auto-Tuner):** Continuously tests and adjusts parameters using recent historical data to adapt to changing market conditions.
* **Setup Blacklist & Tracking:** Rejects statistically poor setups and tracks performance metrics to refine future execution logic.
* **Time-Out Mechanism:** Implements a "Time Stop" feature to automatically exit unprofitable trades that stall, optimizing capital allocation.

## Technology Stack
* **Language:** Python
* **Data Source:** Binance Futures API (or equivalent real-time data streams)
* **Focus Areas:** Data Analysis, Risk Mathematical Modeling, Automated Execution, System Optimization

## Engineering Value
While initially a task automation project, the development of this bot required solving complex engineering challenges similar to those found in aerospace and defense systems:
* Real-time data processing and decision-making under uncertainty.
* Strict risk mitigation protocols (Kill Switches).
* Continuous system optimization (Auto-Tuning) based on feedback loops.

---
*Note: This repository serves as a showcase of system design, algorithmic logic, and Python programming capabilities. Proprietary trading strategies and API keys are not included for security reasons.*
