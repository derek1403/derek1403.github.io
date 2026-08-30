# Proof $\int_{-\infty}^{+\infty} \frac{e^{-x^2} \sin^2(x^2)}{x^2} \mathrm{d}x = \sqrt{\pi} (\sqrt{\phi} - 1)$

+++

## 假設與已知 (Assumptions & Preliminaries)

* **【已知 1】 Integration by Parts：** 

  $$\int u \mathrm{d}v = uv - \int v \mathrm{d}u$$
  
  * 我們令 $u \overset{\text{let}}{=} e^{-x^2} \sin^2(x^2)$，以及 $\mathrm{d}v \overset{\text{let}}{=} \frac{1}{x^2}\mathrm{d}x$ ， $v = -\frac{1}{x}$
  
* **【已知 2】 極限求和 $\frac{\text{finite}}{\text{inf}}$ ：** 

  $$\left[ \frac{e^{-x^2} \sin^2(x^2)}{x} \right]_{-\infty}^{+\infty} = \lim_{x \to \infty} \frac{e^{-x^2} \sin^2(x^2)}{x} - \lim_{x \to \infty} \frac{e^{-x^2} \sin^2(x^2)}{x}=0$$

* **【已知 3】 Double-Angle Formula 倍角公式：** 

  $$\sin(2\theta) = 2\sin(\theta)\cos(\theta) $$

  * 此題中 $\theta$ 是 $x^{2}$
  
* **【已知 4】 Half-Angle Formulas 半角公式：** 

  $$\frac{1-\cos(2\theta)}{2} = \sin^2(\theta) $$

  * 此題中 $\theta$ 是 $x^{2}$

* **【已知 5】 Euler's Formula：** 

  $$ e^{i\theta} = \cos\theta + i\sin\theta $$

  * $\sin\theta = \mathrm{Im}\left[e^{i\theta} \right]$
  * $\cos\theta = \mathrm{Re}\left[e^{i\theta} \right]$
  * 此題中 $\theta$ 是 $2x^{2}$

* **【已知 6】 Gaussian Integral 高斯積分 ：**

  $$I = \int_{-\infty}^{+\infty} e^{-x^2} \mathrm{d}x = \sqrt{\pi} $$

  * 對於有係數的可以使用 $\frac{1}{\sqrt{a}} \sqrt{\pi}$，證明

  $$\begin{gather*}
  ax^2 & \overset{\text{let}}{=}&   \mathbf{X}^2 \\
  a 2x \mathrm{d} x & = & 2 \mathbf{X} \mathrm{d} \mathbf{X}  \\
  \frac{2ax \mathrm{d} x}{2\sqrt{a} x} & = &  \mathrm{d} \mathbf{X}  \\
  \frac{1}{\sqrt{a}} \mathrm{d} x & = &  \mathrm{d} \mathbf{X}
  \end{gather*}$$

  $$\begin{gather*}
  I_a & = &  \int_{-\infty}^{+\infty} e^{-ax^2} \mathrm{d}x \\
  & = &  \frac{1}{\sqrt{a}} \int_{-\infty}^{+\infty} e^{-\mathbf{X}^2} \mathrm{d}\mathbf{X} \\
  & = & \frac{1}{\sqrt{a}} \sqrt{\pi}
  \end{gather*}$$

  * 此題中 $a$ 是 $1-2i$ 和 $1$

* **【已知 7】 轉成複數 $\mathbb{C}$ ：**

  * 複數有最一般的形式 $z = a+bi \in \mathbb{C} , a \in \mathbb{R} \text{ and } b \in \mathbb{R}$ ， 所以可以對 $\sqrt{1+2i} = a +bi$ 解未知數 $a \text{ and } b $
  * 對兩邊平方，係數相同可以得到: $a^2 - b^2 =1$ ； $2ab=2$
  $$\begin{gather*}
  &a^2-\frac{1}{a^2}=1 \\
  \Rightarrow& a^2 = \frac{1}{2} (1 \pm \sqrt{5}) \\
  \Rightarrow& a = \sqrt{\frac{\sqrt{5}+1}{2}} , b= \sqrt{\frac{\sqrt{5}-1}{2}} 
  \end{gather*}$$
  * 所以可以得到 $\mathrm{Im}\left[\sqrt{1+2i}\right] = b$ , $\mathrm{Re}\left[\sqrt{1+2i}\right] = a $

* **【已知 8】 根號相加 ：** 

  $$\begin{gather*}
  &y   &=& \sqrt{4(\sqrt{5}-1)}  + \sqrt{\sqrt{5}+1}\\
  \Rightarrow&y^2 &=&  4(\sqrt{5}-1)+ \sqrt{5}+1 +\sqrt{4(\sqrt{5}-1)}\sqrt{\sqrt{5}+1}\\
  &&=&5\sqrt{5}+5\\
  \Rightarrow&y &=&\sqrt{\sqrt{5}+5} \\
  \end{gather*}$$

* **【已知 9】 Golden Ratio ：** 

  $$\phi = \frac{\sqrt{5}+1}{2}$$

+++

## 證明:

$$\begin{gather*}
\int_{-\infty}^{+\infty} \frac{e^{-x^2} \sin^2(x^2)}{x^2} \mathrm{d}x &\overset{\text{已知 1}}{=}& \left[ -\frac{e^{-x^2} \sin^2(x^2)}{x} \right]_{-\infty}^{+\infty} + \int_{-\infty}^{+\infty} \frac{1}{x} \frac{\mathrm{d}}{\mathrm{d}x} \left( e^{-x^2} \sin^2(x^2) \right) \mathrm{d}x \\
&\overset{\text{已知 2}}{\overset{\text{chain rule}}{=}}& 0 + \int_{-\infty}^{+\infty} \frac{1}{x} \left( -2x e^{-x^2} \sin^2(x^2) + e^{-x^2} 2\sin(x^2)\cos(x^2) \cdot 2x \right) \mathrm{d}x \\
&\overset{\text{已知 3}}{=}& 2 \int_{-\infty}^{+\infty} e^{-x^2} \left( \sin(2x^2) - \sin^2(x^2) \right) \mathrm{d}x \\
&\overset{\text{已知 4}}{=}& 2 \int_{-\infty}^{+\infty} e^{-x^2} \left( \sin(2x^2) - \left( \frac{1-\cos(2x^2)}{2} \right) \right) \mathrm{d}x \\
&\overset{\text{已知 5}}{=}& 2 \int_{-\infty}^{+\infty} e^{-x^2} \left( \mathrm{Im}\left[ e^{i2x^2} \right] - \frac{1}{2}\left( 1 - \mathrm{Re}\left[ e^{i2x^2} \right] \right) \right) \mathrm{d}x \\
&\overset{\text{}}{=}& 2\mathrm{Im} \left[ \int_{-\infty}^{+\infty} e^{-(1-2i)x^2} \mathrm{d}x \right] - \int_{-\infty}^{+\infty} e^{-x^2} \mathrm{d}x + \mathrm{Re} \left[ \int_{-\infty}^{+\infty} e^{-(1-2i)x^2} \mathrm{d}x \right] \\
&\overset{\text{已知 6}}{=}& 2\mathrm{Im} \left[ \sqrt{\frac{\pi}{1-2i}} \,\right] - \sqrt{\pi} + \mathrm{Re} \left[ \sqrt{\frac{\pi}{1-2i}} \,\right]  \\
&\overset{\text{有理化}}{=}& 2\mathrm{Im} \left[ \sqrt{\frac{\pi (1+2i)}{5}} \,\right] - \sqrt{\pi} + \mathrm{Re} \left[ \sqrt{\frac{\pi (1+2i)}{5}} \,\right]  \\
&\overset{\text{}}{=}& \sqrt{\pi} \left( \frac{2}{\sqrt{5}} \mathrm{Im} \left[ \sqrt{1+2i} \,\right] - 1 + \frac{1}{\sqrt{5}}\mathrm{Re} \left[ \sqrt{1+2i}  \, \right]  \right) \\
&\overset{\text{已知 7}}{=}& \sqrt{\pi} \left[ \frac{2}{\sqrt{5}} \sqrt{\frac{\sqrt{5}-1}{2}} - 1 + \frac{1}{\sqrt{5}} \sqrt{\frac{\sqrt{5}+1}{2}}\, \right] \\
&\overset{\text{}}{=}& \sqrt{\pi} \left[ \frac{\sqrt{4(\sqrt{5}-1)}  + \sqrt{\sqrt{5}+1}}{10}  - 1 \,\right] \\
&\overset{\text{已知 8}}{=}& \sqrt{\pi} \left[ \sqrt{\frac{5\sqrt{5}+5}{10}} - 1 \,\right] \\
&\overset{\text{}}{=}& \sqrt{\pi} \left( \sqrt{\frac{\sqrt{5}+1}{2}} - 1 \right) \\
&\overset{\text{已知 9}}{=}& \sqrt{\pi} (\sqrt{\phi} - 1)
\end{gather*}$$



+++
