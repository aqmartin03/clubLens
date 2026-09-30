# clubLens

Initially considered using percentage of distance removed as the primary shot-quality metric. Testing showed this unfairly evaluates long clubs because their purpose differs based on hole length. Changed the design to evaluate shots according to club category and outcome.

During initial prototyping, I considered evaluating shots primarily by percentage of distance removed toward the hole. Testing example shots revealed that this metric did not account for club purpose, hole length, landing position, or intentional target selection. I therefore decided to evaluate performance using multiple shot characteristics rather than distance progress alone.