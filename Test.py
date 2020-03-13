from manimlib.imports import *

class FormalDef(Scene):
    def construct(self):
        whatfa = TextMobject("What is a Finite Automata?")
        defin_text = TextMobject("A Deterministic Finite Automata(DFA), M")
        defin_text2 = TextMobject("is described by the given 5-tuple")
        defin_tex = TexMobject("M = (Q, \\Sigma, \\delta, q_0, \\mathcal{F})")
        where = TexMobject("\\text{Where } Q := \\text{ A finite set of states}")
        sigma = TexMobject("\\Sigma := \\text{A machines alphabet}")
        delta = TexMobject(" \\delta :=\\text{The Transition Function}")
        qnaught = TexMobject("q_0 := \\text{The intial state}")
        finalstates = TexMobject("\\mathcal{F} := \\text{The final or accepting states}")
        group = VGroup(where, sigma, delta, qnaught, finalstates)
        defin_text.shift(UP)
        defin_tex.shift(DOWN)
        group.arrange(DOWN)
        self.play(FadeIn(whatfa))
        self.wait(3)
        self.play(FadeOut(whatfa));
        self.play(FadeIn(defin_text),FadeIn(defin_text2), Write(defin_tex))
        self.wait(5)
        self.play(FadeOut(defin_text),FadeOut(defin_text2))
        self.play(ApplyMethod(defin_tex.shift, 4*UP))
        self.wait(2)
        self.play(FadeIn(where))
        self.play(FadeIn(sigma))
        self.play(FadeIn(delta))
        self.play(FadeIn(qnaught))
        self.play(FadeIn(finalstates))
        self.wait(5)
        self.play(FadeOut(where),FadeOut(sigma),FadeOut(delta),FadeOut(qnaught), FadeOut(finalstates))
        self.play(FadeOut(defin_tex))





class EvenZeros(Scene):
    def construct(self):
        c1 = Circle()
        c2 = Circle()
        c3 = Circle()
        c1.scale(0.5);
        c2.scale(0.4);
        c3.scale(0.4);
        p1 = CurvedArrow(1.25*UP + LEFT, UP*(1.25) + RIGHT)
        p2 = CurvedArrow(DOWN + LEFT, DOWN + RIGHT )
        p3 = CurvedArrow(1.75*RIGHT+0.5*DOWN, 1.75*RIGHT + 0.5*UP, color=MAROON_C)
        p4 = CurvedArrow(2.2*LEFT+0.5*DOWN, 2*LEFT + 0.5*UP,color=MAROON_C)
        p4.scale(-1);
        p1.scale(-1);
        lang = TexMobject("L = \\{ \\omega \\in  {0,1}^n \\mid \\#_0(\\omega) = 2k \\}")
        machine = TexMobject("M = (\\{q_0, q_1\\},\\{0,1\\}, \\delta, q_0,  \\{q_0\\})")
        lang.shift(3*UP)
        machine.shift(3*DOWN)
        q0 = TexMobject("q_0")
        q1 = TexMobject("q_1")
        one1 = TexMobject("1")
        one2 = TexMobject("1")
        zero1 = TexMobject("0")
        zero2 = TexMobject("0")
        one1.next_to(p3,0.5*RIGHT)
        one2.next_to(p4, 0.5*LEFT)
        zero1.next_to(p1, 0.5*UP)
        zero2.next_to(p2, 0.5*DOWN)
        q0.shift(LEFT)
        q1.shift(RIGHT)
        c1.shift(RIGHT)
        c2.shift(LEFT)
        c3.surround(c2);
        self.play(Write(lang))
        self.wait(5)
        self.play(GrowFromCenter(c1));
        self.play(GrowFromCenter(c2), GrowFromCenter(c3));
        self.play(FadeIn(p1), FadeIn(p2));
        self.play(GrowArrow(p3), GrowArrow(p4))
        self.play(Write(q0), Write(q1), FadeIn(one1), FadeIn(one2));
        self.play(FadeIn(zero1), FadeIn(zero2))
        self.wait(2)
        self.play(FadeIn(machine));
        self.wait(5);
