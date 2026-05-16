# Goodhart's Law: When Metrics Become Targets

In any organization, we use metrics to track progress. We measure "lines of code written" to judge programmer productivity, "number of calls handled" to evaluate call center agents, or "test scores" to determine student intelligence.

The logic seems sound: if you want more of something, you should measure it and reward those who achieve higher numbers. However, this approach often backfires due to a phenomenon known as **Goodhart's Law**.

## 1. What is Goodhart's Law?
Goodhart's Law is an adage stating: **"When a measure becomes a target, it ceases to be a good measure."**

Named after British economist Charles Goodhart, the law describes how people will "game the system" to optimize for the metric being measured, often at the expense of the actual goal the metric was intended to represent.

## 2. The Mechanics of "Gaming the System"
The core of the problem is the difference between a **Proxy** and the **Goal**.

- **The Goal:** The actual outcome you want (e.g., "High-quality software").
- **The Proxy:** The measurable metric used to track the goal (e.g., "Number of features shipped per month").

When you reward the proxy, people stop focusing on the goal and start focusing on the proxy. They find the path of least resistance to increase the number, even if it harms the overall quality.

## 3. Real-World Examples

### In Software Engineering
Suppose a manager decides to measure productivity by the **number of lines of code (LOC)** written per day.
- **The Goal:** Build a robust, efficient application.
- **The Proxy:** Lines of Code.
- **The Result:** Programmers start writing bloated, verbose code. They avoid using efficient libraries or simplifying their logic because doing so would *decrease* their LOC count. The metric goes up, but the software becomes harder to maintain and more prone to bugs.

### In Education
A school district decides to judge teacher quality based on **student standardized test scores**.
- **The Goal:** Ensure students are learning and developing critical thinking skills.
- **The Proxy:** Test Scores.
- **The Result:** "Teaching to the test." Teachers stop covering the broader curriculum and spend all their time drilling students on the specific formats and tricks needed to pass the test. The scores rise, but the students' actual understanding of the subject declines.

### In Fast Food
A restaurant chain measures efficiency by how quickly an order is "cleared" from the digital screen after it is prepared.
- **The Goal:** Get food to customers quickly.
- **The Proxy:** Screen Clear Time.
- **The Result:** Staff begin clearing orders from the screen *before* the food is actually ready. On paper, the "service time" looks incredible, but the customers are still waiting at the counter for their food.

## 4. How to Avoid Goodhart's Law
You cannot stop people from trying to optimize for rewards, but you can design better measurement systems.

### 1. Use a "Balanced Scorecard" (Multiple Metrics)
Never rely on a single metric to measure a complex outcome. If you measure "Speed," you must also measure "Quality" and "Accuracy."
- If you track "Lines of Code," also track "Bug Density" and "Peer Review Approval."
- If you track "Call Volume," also track "Customer Satisfaction (CSAT)."
When metrics conflict, gaming the system becomes much harder.

### 2. Measure Outcomes, Not Activities
Focus on the final result rather than the steps taken to get there.
- Instead of measuring "Hours Worked" (Activity), measure "Project Milestones Achieved" (Outcome).
- Instead of "Number of Sales Calls" (Activity), measure "Revenue Generated" (Outcome).

### 3. Maintain Flexibility
Recognize that every metric is a temporary approximation. Periodically review your targets and ask: *"Is this metric still representing the goal, or have we started optimizing for the metric itself?"*

## Summary: The Danger of the Number
Goodhart's Law reminds us that numbers are a map, not the territory. When we treat a metric as the goal, we stop seeing the reality of the work and start seeing only the numbers. To succeed, focus on the *intent* behind the measure, not just the measure itself.
