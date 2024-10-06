from manim import *

class intro(Scene):
    def construct(self):
        self.wait()

        quadratic_formula = MathTex(
            r"f(x)=ax^2+bx+c",
            substrings_to_isolate=[
                "a", "b", "c"
                ]
            )
        
        quadratic_formula.set_color_by_tex(
            "a", YELLOW).set_color_by_tex(
            "b", BLUE).set_color_by_tex(
            "c", RED).shift(
            DOWN * 1.2).scale(2)
        
        title_intro = Tex(
            r"Funções do segundo grau"
        ).scale(2)

        subtitle_intro = Tex(
            r"Roteiro e animações por \textit{Yago Almeida Pessoa}").scale(0.6).next_to(
            title_intro, DOWN
        )
        
        vg_title = VGroup(title_intro, subtitle_intro).shift(UP * 2)
        axes_intro = Axes(x_range=[-0.5, 5], y_range=[-0.5, 2.5]).add_coordinates().set_opacity(0.2)
        axes_intro_labels = axes_intro.get_axis_labels(x_label="x", y_label="f(x)").set_opacity(0.2)
        graph_intro1 = axes_intro.plot(
            lambda x: (-0.5 * x ** 2) + 2 * x, x_range=[-0.1, 4.1], color=RED, stroke_opacity=0.2
        )
        self.play(
            Create(axes_intro),
            Write(axes_intro_labels),
            Create(graph_intro1)
        )
        self.play(
            Write(vg_title),
            run_time=1.3
        )
        self.play(
            Write(quadratic_formula),
            run_time=2
        )
        self.wait(4)
        self.play(
            Unwrite(quadratic_formula),
            Unwrite(title_intro),
            Unwrite(subtitle_intro),
            Uncreate(axes_intro),
            Unwrite(axes_intro_labels),
            Uncreate(graph_intro1),
            run_time=1.3
        )
        self.wait()
class intro2(Scene):
    def construct(self):
        self.wait()
        num_plane = NumberPlane()
        definition = Tex(r'Definição formal').scale(3)
        quadratic_formula = MathTex("f","(x)","=","a","x^2","+","b","x","+","c")
        quadratic_formula2 = MathTex("f","(x)","=","x","(","a","x","+","b",")")
        addicional_content = MathTex("a",",","b",",","c",r"\in",r"\mathbb{R}",r"\land","a",r"\neq","0")
        addicional_content[0].set_color(YELLOW)
        addicional_content[8].set_color(YELLOW)
        addicional_content[2].set_color(BLUE)
        addicional_content[4].set_color(RED)
        self.play(Write(definition),run_time=0.5)
        self.wait(3)
        self.play(definition.animate.shift(UP*3.5+LEFT*4.7).scale(0.4))
        self.wait(2)
        self.play(Write(quadratic_formula.scale(2.5)))
        self.wait(3)
        self.play(quadratic_formula.animate.shift(UP * 1.5))
        self.play(quadratic_formula.animate.set_color_by_tex("a", YELLOW).set_color_by_tex("b", BLUE).set_color_by_tex("c", RED))
        self.play(Write(addicional_content.shift(DOWN*1.5).scale(2.5)))
        self.wait(4)
        self.play(FadeOut(addicional_content),quadratic_formula.animate.set_color_by_tex("a", WHITE).set_color_by_tex("b", WHITE).set_color_by_tex("c", WHITE).shift(DOWN*1.5))
        self.wait(2)
        self.play(Indicate(quadratic_formula[4]))
        self.wait()
        self.play(Indicate(quadratic_formula[7]))
        self.wait(2)
        self.play(TransformMatchingTex(quadratic_formula,quadratic_formula2.scale(2.5)))
        self.wait(3)
        self.play(FadeOut(quadratic_formula2),FadeOut(definition))
class graphics(Scene):
    def construct(self):
        self.wait()
        y_range_min,y_range_max = -4,4
        x_range_min,x_range_max = -4,4
        num_plane = NumberPlane(
            x_range=[x_range_min, x_range_max, 1],
            x_length=4.55,
            y_range=[y_range_min, y_range_max, 1],
            y_length=4.55,
            background_line_style={"stroke_opacity": 0.2}
        ).shift(LEFT * 4.55)
        a,b,c = ValueTracker(1),ValueTracker(0),ValueTracker(0)
        graph_demo_title = Tex(r'Gráfico da função').scale(3)
        axes_graph_demo = Axes(
            x_range=[x_range_min, x_range_max, 1],
            y_range=[y_range_min, y_range_max, 1],
            y_length=4.55,
            x_length=4.55,
            axis_config={
                "font_size": 20,
                "include_tip": False
            }
        ).shift(LEFT * 4.55).add_coordinates()
        axes_gd_labels = axes_graph_demo.get_axis_labels(
            x_label="x",
            y_label="f(x)"
        )
        axes_gd_labels[0].set_font_size(34)
        axes_gd_labels[1].set_font_size(34)
        axes_gd_labels[0].next_to(axes_graph_demo.get_x_axis(), RIGHT, buff=0.1)
        axes_gd_labels[1].next_to(axes_graph_demo.get_y_axis(), UP, buff=0.1)
        def get_x_for_y_boundaries(a_val, b_val, c_val, y_min, y_max):
            from math import sqrt
            # Quadratic formula discriminant: b² - 4ac
            discriminant_max = b_val**2 - 4 * a_val * (c_val - y_max)
            discriminant_min = b_val**2 - 4 * a_val * (c_val - y_min)
            def calc_roots(discriminant, a_val, b_val):
                if discriminant < 0:
                    return None, None  # No real roots
                else:
                    sqrt_disc = sqrt(discriminant)
                    x_pos = (-b_val + sqrt_disc) / (2 * a_val)
                    x_neg = (-b_val - sqrt_disc) / (2 * a_val)
                    return x_pos, x_neg
            x_max_pos, x_max_neg = calc_roots(discriminant_max, a_val, b_val)
            x_min_pos, x_min_neg = calc_roots(discriminant_min, a_val, b_val)
            x_values = [x for x in [x_min_neg, x_min_pos, x_max_neg, x_max_pos] if x is not None]
            valid_x_range = [x for x in x_values if x_range_min <= x <= x_range_max]
            if not valid_x_range:
                valid_x_range = [x_range_min, x_range_max]
            return valid_x_range
        graph_demo = always_redraw(lambda: axes_graph_demo.plot(
            lambda x: a.get_value() * x**2 + b.get_value() * x + c.get_value(),
            x_range=get_x_for_y_boundaries(a.get_value(), b.get_value(), c.get_value(), y_range_min, y_range_max)
        ).set_color(PURPLE))
        
        # Label stuff
        end_point = graph_demo.get_end()
        label_graph = MathTex("x^2").next_to(end_point,RIGHT+DOWN).set_color(PURPLE).scale(0.5)
        label_graph.add_updater(
            lambda mob: mob.next_to(end_point,RIGHT+DOWN).set_color(PURPLE).scale(0.5)
        )

        self.play(Create(graph_demo_title), run_time=0.5)
        self.wait(3)
        self.play(graph_demo_title.animate.shift(UP * 3.5 + LEFT * 4.7).scale(0.4))
        self.wait(2)
        self.play(Create(axes_graph_demo), Write(axes_gd_labels), FadeIn(num_plane))
        self.wait()
        self.play(Create(graph_demo), Write(label_graph))
        self.wait()
        self.play(a.animate.set_value(-1), run_time=3)
        self.wait()