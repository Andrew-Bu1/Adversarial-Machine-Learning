from art.attacks.evasion import HopSkipJump
from base_attack import BaseAttack

class HopSkipJumpAttack(BaseAttack):
    def __init__(self, classifier, targeted=True):
        self.model = HopSkipJumpAttack(classifier=classifier, targeted=targeted)

    def generate(self, x, y):
        return self.model.generate(x, y) 

