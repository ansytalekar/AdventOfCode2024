# Recursive loop checker for Day 5 Advent
class LoopChecker:
    def __init__(self):
        self.storage() = set();
        self.recursive() = set();

    def loop_check(self, rules_dict, rule, storage, recursive):
        storage.add(rule);
        recursive.add(rule);

        for component in rules_dict[rule]:
            if component not in storage:
                if self.loop_check(rules_dict, component, storage, recursive):
                    return True;
            elif component in recursive:
                return True;

        recursive.remove(rule);
        return False;

    def strip_dict(self, rules):
        for rule in rules:
            if rule not in self.storage:
                if self.loop_check(rules, rule, self.storage, self.recursive):
                    return True;
        
        return False;