# clubLens

Hello, there!

If you are on this page, you have found my product "clubLens". The intent of this product is to apply my knowledge of programming toward a something that is intended to help with a real problem many people have: where their golf swing is going wrong!

"clubLens" is intended to become a website and then eventually a mobile app one day. To progress this product, here is the tech stack I have been using: Python, SQL (specifically SQLite), HTML, and CSS.

By using this chosen tech stack, my intent is to use technology to create an algorithm that advises golfers on how to improve their golf shots. At first, the golfer will have to input their data into the program, and then it will eventually advance into a more functional product.

Below is some documentation I have been making along the way. Enjoy!

Project Documentation:
Initially considered using percentage of distance removed as the primary shot-quality metric. Testing showed this unfairly evaluates long clubs because their purpose differs based on hole length. Changed the design to evaluate shots according to club category and outcome.

During initial prototyping, I considered evaluating shots primarily by percentage of distance removed toward the hole. Testing example shots revealed that this metric did not account for club purpose, hole length, landing position, or intentional target selection. I therefore decided to evaluate performance using multiple shot characteristics rather than distance progress alone.
