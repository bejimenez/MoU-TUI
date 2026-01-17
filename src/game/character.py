"""
Character data structures for Ulan RPG.
"""

from dataclasses import dataclass, field


@dataclass
class Character:
    """Player character data"""
    name: str = ""
    
    # D&D stats (base starts at 8 for point-buy)
    strength: int = 8
    dexterity: int = 8
    constitution: int = 8
    intelligence: int = 8
    wisdom: int = 8
    charisma: int = 8
    
    # Ulan-specific
    divine_fervor: int = 5  # 1-10 scale, starts at middle
    
    # Loyalty system (populated during gameplay)
    loyalty: dict[str, int] = field(default_factory=dict)
    
    @property
    def total_stat_points(self) -> int:
        """Calculate total points spent on stats"""
        return (self.strength + self.dexterity + self.constitution + 
                self.intelligence + self.wisdom + self.charisma)
    
    @property
    def points_spent(self) -> int:
        """Calculate how many points have been spent using point-buy rules"""
        stats = [self.strength, self.dexterity, self.constitution,
                self.intelligence, self.wisdom, self.charisma]
        
        total = 0
        for stat in stats:
            total += self._stat_cost(stat)
        return total
    
    @staticmethod
    def _stat_cost(value: int) -> int:
        """
        Calculate point cost for a stat value using D&D 5e point-buy.
        Base is 8, costs increase at higher values.
        """
        if value < 8:
            return 0
        elif value <= 13:
            return value - 8
        elif value == 14:
            return 7  # 13 costs 5, +2 more for 14
        elif value == 15:
            return 9  # 14 costs 7, +2 more for 15
        else:
            return 9  # Cap at 15
    
    @property
    def points_remaining(self) -> int:
        """Points remaining in point-buy (27 total)"""
        return 27 - self.points_spent
    
    def can_increase_stat(self, stat_name: str) -> bool:
        """Check if a stat can be increased (max 15, must have points)"""
        current_value = getattr(self, stat_name)
        if current_value >= 15:
            return False
        
        # Check if we have enough points for the increase
        cost_diff = self._stat_cost(current_value + 1) - self._stat_cost(current_value)
        return self.points_remaining >= cost_diff
    
    def can_decrease_stat(self, stat_name: str) -> bool:
        """Check if a stat can be decreased (min 8)"""
        current_value = getattr(self, stat_name)
        return current_value > 8