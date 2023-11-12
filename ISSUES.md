<h1 align="center">Issue Tracker</h1>
<p align="center">
  World's Okayest Group
</p>

### Table of Contents
- [Prelude](#prelude)
- [Jerk](#jerk)
- [Precision](#precision)

### Prelude
This is the issue tracker for the project. Issues can be theorized or actual, and solutions should be proposed as they come along.

### Jerk
As a result of the equations used to map velocity over time, we have found that it's expected to have a harsh jump that levels off as the vehicle approaches the set speed.
For acceleration, we are utilizing the solution to a seperable ODE of the form:

$V_{1}(t) = \frac{V_{s}}{1+\frac{V_{s}-V_0}{V_0} *e^{-t\alpha_{1}}}$

With $\alpha_{1}$ defined as:

$\alpha_{1} = -\frac{1}{t}ln((\frac{V_{s}}{V_{s}-\varepsilon}-1)(\frac{V_{0}}{V_{s}-V_{0}}))$

For deceleration, we are using:

$V_{2}(t) = \frac{V_{s}}{1+\frac{V_{s}-V_{0}}{V_0} *e^{-t\alpha_{2}}}$

With $\alpha_{2}$ defined as:

$\alpha_{2} = -\frac{1}{t}ln((\frac{V_{s}}{V_{s}+\varepsilon}-1)(\frac{V_{0}}{V_{s}-V_{0}}))$

Where $t$ is time in seconds, $V_{s}$ is the set velocity, $V_{0}$ is the initial velocity, and $\varepsilon$ is the single precision machine epsilon.


These equations, when plugged into graphing calculators, yield:

<p align="center">
	<img alt="Graphic Velocity Display" src="https://i.imgur.com/Gc9Bdbn.png"/>
</p>
With the green function representing deceleration, and the black function representing acceleration over a $t$ of 2 seconds.

As a result, we expect extreme jerk to occur. We believe an effective solution will be to quadratically increase time allotments based on magnitude of change between
set and inital velocity, with a point set at the initial velocity and the graph interpolated with that point at at a discretization rate of 0.1. 


### Precision and Singularity

We are currently encountering an issue with the ego vehicle having a singularity at $t$ = 0.25, where the derivative becomes non-finite. We believe this to be because it is being fed an
input of -0.5, which will in turn cause a asymptote at the point. We may also be encountering subtractive cancellation in our precision, which could lead to a massive amount of error.
We are pursuing further advice regarding a solution to this, as we are unsure of the problem and unable to effectively diagnose it ourselves.
