from manim import *  # type: ignore


class CLT(Scene):
    def construct(self):
        text = Text("Central Limit Theorem").to_edge(UP)

        desc = Text("In probability theory, the central limit theorem establishes that, in many situations,\n"
                    "when independent random variables are summed up, their properly normalized sum\n"
                    "tends toward a normal distribution even if the original variables themselves\n"
                    "are not normally distributed.",
                    t2c={'probability theory': BLUE,
                         'central limit theorem': BLUE,
                         'independent random variables': RED,
                         'normal distribution': BLUE,
                         'even if the original variables themselves': GREEN_B,
                         'are not normally distributed': GREEN_B},
                    font_size=DEFAULT_FONT_SIZE/2.,
                    line_spacing=LARGE_BUFF)

        source = Text("- Wikipedia", font_size=DEFAULT_FONT_SIZE/2.5)

        desc.next_to(text, DOWN * 2)
        source.next_to(desc, DOWN * 2, aligned_edge=DR)

        self.play(Write(text))
        self.play(FadeIn(desc, lag_ratio=0.1, run_time=6))
        self.play(Write(source))
        self.clear()

        text = Text("(Discrete) Uniform Distribution").to_edge(UP)
        problem = Text("A fair six-sided die is distributed uniformly",
                       t2c={'fair': BLUE, 'distributed': BLUE, 'uniformly': RED},
                       font_size=DEFAULT_FONT_SIZE/2.)
        formula = MathTex("X \\sim \\mathcal{U}(a, b)")
        pmf = MathTex("P(X = x) = \\frac{1}{n}")

        VGroup(problem, formula, pmf).arrange(DOWN, center=False).next_to(
            text, direction=DOWN * 2)

        self.play(Write(text))
        self.play(FadeIn(problem, lag_ratio=0.1, run_time=2))
        self.play(Write(formula), Write(pmf))

        new_formula = MathTex("X \\sim \\mathcal{U}(1, 6)")
        new_pmf = MathTex("P(X = x) = \\frac{1}{6}, x \\in [1, 6]")

        VGroup(problem, new_formula, new_pmf).arrange(DOWN, center=False).next_to(
            text, direction=DOWN * 2)

        self.play(Transform(formula, new_formula), Transform(pmf, new_pmf))

        question = Text("How is the average of two dice rolls distributed?",
                        t2c={'sum': BLUE, 'distributed': BLUE},
                        font_size=DEFAULT_FONT_SIZE/2.)

        question.next_to(pmf, DOWN)

        self.play(Write(question))
        self.wait()
