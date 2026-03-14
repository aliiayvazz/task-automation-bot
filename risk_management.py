# risk_management.py
# This module handles dynamic position sizing and daily risk limits (Kill Switch).
# Proprietary logic and specific margin thresholds are removed for security.

class RiskManager:
    def __init__(self, daily_loss_limit_usd=100.0, max_account_risk_pct=0.02):
        """
        Initializes the risk management module.
        :param daily_loss_limit_usd: Maximum allowed loss per day before triggering Kill Switch.
        :param max_account_risk_pct: Maximum percentage of total account balance to risk on a single trade.
        """
        self.daily_loss_limit = daily_loss_limit_usd
        self.max_account_risk = max_account_risk_pct
        self.current_daily_loss = 0.0
        self.is_kill_switch_active = False

    def check_kill_switch(self, current_loss: float) -> bool:
        """
        Evaluates if the daily loss limit has been breached.
        """
        self.current_daily_loss += current_loss
        
        if self.current_daily_loss >= self.daily_loss_limit:
            self.is_kill_switch_active = True
            print(f"CRITICAL: Kill Switch Activated! Daily loss limit ({self.daily_loss_limit}$) reached.")
            return True
        return False

    def calculate_position_size(self, account_balance: float, stop_loss_pct: float, setup_probability: float) -> float:
        """
        Edge-Based Sizing: Calculates position size dynamically based on setup quality.
        """
        if self.is_kill_switch_active:
            print("Action Denied: Kill switch is currently active.")
            return 0.0

        if stop_loss_pct <= 0:
             raise ValueError("Stop loss percentage must be greater than zero.")

        # Base risk amount
        base_risk_amount = account_balance * self.max_account_risk
        
        # Adjust risk based on setup probability (Edge factor)
        # Higher probability setups get slightly larger size, lower probability get smaller.
        edge_multiplier = setup_probability / 0.50 # Assuming 50% is baseline
        adjusted_risk_amount = base_risk_amount * edge_multiplier

        # Calculate final position size
        position_size = adjusted_risk_amount / stop_loss_pct
        
        return round(position_size, 2)

# Example Usage (For demonstration purposes only):
# if __name__ == "__main__":
#     rm = RiskManager(daily_loss_limit_usd=150.0)
#     size = rm.calculate_position_size(account_balance=1000, stop_loss_pct=0.05, setup_probability=0.65)
#     print(f"Calculated Position Size: {size}")
