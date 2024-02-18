import sys
import os

from clause.data.triples import TripleSet
from clause.util.utils import get_base_dir

from clause.rule.rules import RuleSet
from clause.rule.ruleparser import RuleReader

# *** Example of how to process and merge rule sets independent of c_clause ***

path_train = f"{get_base_dir()}/data/wnrr/train.txt"
path_valid = f"{get_base_dir()}/data/wnrr/valid.txt"
path_test  = f"{get_base_dir()}/data/wnrr/test.txt"

path_rules_in1 = f"{get_base_dir()}/data/wnrr/anyburl-rules-c5-3600"

# run demo-torm.py first to generate this file
path_rules_in2 = f"{get_base_dir()}/local/myrules/rules-torm.txt"
    
path_rules_out = f"{get_base_dir()}/local/myrules/combined-rules.txt"
triples = TripleSet(path_train)

# load an anyburl ruleset and remove all rules that are not B rules
rules_b = RuleSet(triples.index)
rule_reader = RuleReader(rules_b)
rule_reader.read_file(path_rules_in1)
rules_b.retainOnly("B")

# load an nanytorm ruleset that contains not B rules
rules_other = RuleSet(triples.index)
rule_reader = RuleReader(rules_other)
rule_reader.read_file(path_rules_in2)
rules_other.retainOnly("Uc", "Ud", "XXuc", "XXud", "Z")

# and the anyburl rules to the other rule set
rules_other.add_ruleset(rules_b)

# write the combined ruleset to a file
rules_other.write(path_rules_out)
