from art.attacks.evasion import SignOPTAttack
from base_attack import BaseAttack

class SignOptAttack(BaseAttack):
    def __init__(self, classifier, targeted=True):
        self.model = SignOPTAttack(classifier=classifier, targeted=targeted)

    def generate(self, x, y):
        return self.model.generate(x, y) 

