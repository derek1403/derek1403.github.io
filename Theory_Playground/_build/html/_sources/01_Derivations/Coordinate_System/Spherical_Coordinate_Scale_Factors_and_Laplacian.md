# Spherical Coordinate Scale Factors and Laplacian (球座標的尺度因子、體積元素與拉普拉斯算子)

+++

## 證明目標:

從卡氏座標 $(x,y,z)$ 與球座標 $(r,\theta,\phi)$ 的變數變換出發，逐式證明下列五件事：

* (a) 三個尺度因子為 $h_r = 1$、$h_\theta = r$、$h_\phi = r\sin\theta$，且三個基底向量彼此正交。
* (b) 體積元素為

  $$dV = r^2 \sin\theta \, dr \, d\theta \, d\phi$$

* (c) 梯度算子為

  $$\nabla f = \frac{\partial f}{\partial r}\hat{e}_r + \frac{1}{r}\frac{\partial f}{\partial \theta}\hat{e}_\theta + \frac{1}{r\sin\theta}\frac{\partial f}{\partial \phi}\hat{e}_\phi$$

* (d) 散度算子為

  $$\nabla \cdot \vec{A} = \frac{1}{r^2}\frac{\partial}{\partial r}\left[ r^2 A_r \right] + \frac{1}{r\sin\theta}\frac{\partial}{\partial \theta}\left[ \sin\theta \, A_\theta \right] + \frac{1}{r\sin\theta}\frac{\partial A_\phi}{\partial \phi}$$

* (e) 拉普拉斯算子為

  $$\nabla^2 f = \frac{1}{r^2}\frac{\partial}{\partial r}\left[ r^2 \frac{\partial f}{\partial r} \right] + \frac{1}{r^2 \sin\theta}\frac{\partial}{\partial \theta}\left[ \sin\theta \frac{\partial f}{\partial \theta} \right] + \frac{1}{r^2 \sin^2\theta}\frac{\partial^2 f}{\partial \phi^2}$$

+++

## 假設與已知 (Assumptions & Preliminaries)

* **【定義 1】 球狀極座標 (Spherical polar coordinates)：** 以 $r$ 為到原點的距離、$\theta$ 為與 $z$ 軸的夾角、$\phi$ 為投影到 $xy$ 平面後與 $x$ 軸的夾角。

  $$\begin{gather*}
  x &\overset{\text{def}}{=}& r\sin\theta\cos\phi \\
  y &\overset{\text{def}}{=}& r\sin\theta\sin\phi \\
  z &\overset{\text{def}}{=}& r\cos\theta
  \end{gather*}$$

  * $r$ : 到原點的距離 (Radial distance) $[\text{m}]$，$0 \le r < \infty$
  * $\theta$ : 天頂角 (Polar / zenith angle) $[\text{rad}]$，$0 \le \theta \le \pi$
  * $\phi$ : 方位角 (Azimuthal angle) $[\text{rad}]$，$0 \le \phi < 2\pi$
  * $x, y, z$ : 卡氏座標分量 (Cartesian components) $[\text{m}]$

* **【定義 2】 位置向量 (Position vector)：** 把【定義 1】寫成向量形式。

  $$\vec{r} \overset{\text{def}}{=} r\sin\theta\cos\phi \, \hat{i} + r\sin\theta\sin\phi \, \hat{j} + r\cos\theta \, \hat{k}$$

  * $\vec{r}$ : 位置向量 (Position vector) $[\text{m}]$
  * $\hat{i}, \hat{j}, \hat{k}$ : 卡氏單位基底 (Cartesian unit basis) $[\text{無單位}]$，為**與位置無關的常向量**

* **【定義 3】 尺度因子與曲線座標單位基底 (Scale factors and curvilinear unit basis)：** 令 $(q_1, q_2, q_3) \overset{\text{def}}{=} (r, \theta, \phi)$。

  $$\begin{gather*}
  h_i &\overset{\text{def}}{=}& \left| \frac{\partial \vec{r}}{\partial q_i} \right| \\
  \hat{e}_i &\overset{\text{def}}{=}& \frac{1}{h_i}\frac{\partial \vec{r}}{\partial q_i}
  \end{gather*}$$

  * $h_i$ : 第 $i$ 個座標的尺度因子 (Scale factor)，把座標增量 $dq_i$ 換算成實際弧長
  * $\hat{e}_i$ : 第 $i$ 個座標方向的單位基底 (Unit basis vector) $[\text{無單位}]$
  * $q_i$ : 第 $i$ 個曲線座標 (Curvilinear coordinate)

* **【已知 1】 全微分（鏈鎖律）(Total differential / chain rule)：** 位置向量沿座標變動所掃出的線元素。

  $$d\vec{r} = \frac{\partial \vec{r}}{\partial q_1}dq_1 + \frac{\partial \vec{r}}{\partial q_2}dq_2 + \frac{\partial \vec{r}}{\partial q_3}dq_3$$

  * $d\vec{r}$ : 線元素 (Line element) $[\text{m}]$
  * $dq_i$ : 第 $i$ 個座標的微小增量 (Coordinate increment)

* **【已知 2】 梯度的定義性質 (Defining property of the gradient)：** 純量場的全微分等於梯度與線元素的內積。

  $$df = \nabla f \cdot d\vec{r}$$

  * $f$ : 任意可微純量場 (Scalar field)
  * $\nabla f$ : $f$ 的梯度 (Gradient)

* **【已知 3】 散度的通量定義 (Flux definition of the divergence)：** 散度是單位體積的淨外向通量。

  $$\nabla \cdot \vec{A} \overset{\text{def}}{=} \lim_{\Delta V \to 0} \frac{1}{\Delta V}\oint_{S} \vec{A}\cdot d\vec{S}$$

  * $\vec{A}$ : 任意可微向量場 (Vector field)
  * $\Delta V$ : 包住該點的微小體積 (Infinitesimal volume) $[\text{m}^3]$
  * $d\vec{S}$ : 該體積邊界上的外向面元素 (Outward area element) $[\text{m}^2]$

* **【已知 4】 拉普拉斯算子的定義 (Definition of the Laplacian)：**

  $$\nabla^2 f \overset{\text{def}}{=} \nabla \cdot \left( \nabla f \right)$$

* **【已知 5】 畢氏三角恆等式 (Pythagorean trigonometric identity)：**

  $$\sin^2 \alpha + \cos^2 \alpha = 1$$

  * $\alpha$ : 任意角 (Arbitrary angle) $[\text{rad}]$

* **【推導 1】 位置向量對三個座標的偏微分 (Partial derivatives of the position vector)：** 把【定義 2】逐項微分；$\hat{i},\hat{j},\hat{k}$ 為常向量，故不被微分。

  * (a) 對 $r$ 微分（$r$ 以外的兩個座標視為常數）：

  $$\begin{gather*}
  \frac{\partial \vec{r}}{\partial r} &\overset{\text{定義 2}}{=}& \frac{\partial}{\partial r}\left[ r\sin\theta\cos\phi \, \hat{i} + r\sin\theta\sin\phi \, \hat{j} + r\cos\theta \, \hat{k} \right] \\
  &=& \sin\theta\cos\phi \, \hat{i} + \sin\theta\sin\phi \, \hat{j} + \cos\theta \, \hat{k}
  \end{gather*}$$

  * (b) 對 $\theta$ 微分：

  $$\begin{gather*}
  \frac{\partial \vec{r}}{\partial \theta} &\overset{\text{定義 2}}{=}& \frac{\partial}{\partial \theta}\left[ r\sin\theta\cos\phi \, \hat{i} + r\sin\theta\sin\phi \, \hat{j} + r\cos\theta \, \hat{k} \right] \\
  &=& r\cos\theta\cos\phi \, \hat{i} + r\cos\theta\sin\phi \, \hat{j} - r\sin\theta \, \hat{k}
  \end{gather*}$$

  * (c) 對 $\phi$ 微分（$z = r\cos\theta$ 完全不含 $\phi$，故第三項為零）：

  $$\begin{gather*}
  \frac{\partial \vec{r}}{\partial \phi} &\overset{\text{定義 2}}{=}& \frac{\partial}{\partial \phi}\left[ r\sin\theta\cos\phi \, \hat{i} + r\sin\theta\sin\phi \, \hat{j} + r\cos\theta \, \hat{k} \right] \\
  &=& -r\sin\theta\sin\phi \, \hat{i} + r\sin\theta\cos\phi \, \hat{j}
  \end{gather*}$$

+++

## 證明:

### (a) proof 尺度因子與正交性 (Scale factors and orthogonality)

* (a-1) 三個尺度因子：

$$\begin{gather*}
h_r &\overset{\text{定義 3}}{=}& \left| \frac{\partial \vec{r}}{\partial r} \right| \\
&\overset{\text{推導 1(a)}}{=}& \left( \sin^2\theta\cos^2\phi + \sin^2\theta\sin^2\phi + \cos^2\theta \right)^{1/2} \\
&=& \left[ \sin^2\theta\left( \cos^2\phi + \sin^2\phi \right) + \cos^2\theta \right]^{1/2} \\
&\overset{\text{已知 5}}{=}& \left( \sin^2\theta + \cos^2\theta \right)^{1/2} \\
&\overset{\text{已知 5}}{=}& 1
\end{gather*}$$

$$\begin{gather*}
h_\theta &\overset{\text{定義 3}}{=}& \left| \frac{\partial \vec{r}}{\partial \theta} \right| \\
&\overset{\text{推導 1(b)}}{=}& \left( r^2\cos^2\theta\cos^2\phi + r^2\cos^2\theta\sin^2\phi + r^2\sin^2\theta \right)^{1/2} \\
&=& r\left[ \cos^2\theta\left( \cos^2\phi + \sin^2\phi \right) + \sin^2\theta \right]^{1/2} \\
&\overset{\text{已知 5}}{=}& r\left( \cos^2\theta + \sin^2\theta \right)^{1/2} \\
&\overset{\text{已知 5}}{=}& r
\end{gather*}$$

$$\begin{gather*}
h_\phi &\overset{\text{定義 3}}{=}& \left| \frac{\partial \vec{r}}{\partial \phi} \right| \\
&\overset{\text{推導 1(c)}}{=}& \left( r^2\sin^2\theta\sin^2\phi + r^2\sin^2\theta\cos^2\phi \right)^{1/2} \\
&=& r\sin\theta\left( \sin^2\phi + \cos^2\phi \right)^{1/2} \\
&\overset{\text{已知 5}}{=}& r\sin\theta
\end{gather*}$$

* (a-2) 三個基底方向兩兩正交：

$$\begin{gather*}
\frac{\partial \vec{r}}{\partial r}\cdot\frac{\partial \vec{r}}{\partial \theta} &\overset{\text{推導 1(a)(b)}}{=}& r\sin\theta\cos\theta\cos^2\phi + r\sin\theta\cos\theta\sin^2\phi - r\cos\theta\sin\theta \\
&\overset{\text{已知 5}}{=}& r\sin\theta\cos\theta - r\sin\theta\cos\theta \\
&=& 0
\end{gather*}$$

$$\begin{gather*}
\frac{\partial \vec{r}}{\partial r}\cdot\frac{\partial \vec{r}}{\partial \phi} &\overset{\text{推導 1(a)(c)}}{=}& -r\sin^2\theta\cos\phi\sin\phi + r\sin^2\theta\sin\phi\cos\phi \\
&=& 0
\end{gather*}$$

$$\begin{gather*}
\frac{\partial \vec{r}}{\partial \theta}\cdot\frac{\partial \vec{r}}{\partial \phi} &\overset{\text{推導 1(b)(c)}}{=}& -r^2\sin\theta\cos\theta\cos\phi\sin\phi + r^2\sin\theta\cos\theta\sin\phi\cos\phi \\
&=& 0
\end{gather*}$$

故 $\{\hat{e}_r, \hat{e}_\theta, \hat{e}_\phi\}$ 為一組**正交歸一**基底，(b)–(e) 皆建立在此正交性上。

### (b) proof 體積元素 (Volume element)

把【已知 1】的線元素用【定義 3】改寫，微小盒子的三個邊向量即為 $h_i \, dq_i \, \hat{e}_i$：

$$\begin{gather*}
d\vec{r} &\overset{\text{已知 1}}{=}& \frac{\partial \vec{r}}{\partial q_1}dq_1 + \frac{\partial \vec{r}}{\partial q_2}dq_2 + \frac{\partial \vec{r}}{\partial q_3}dq_3 \\
&\overset{\text{定義 3}}{=}& h_1 \, dq_1 \, \hat{e}_1 + h_2 \, dq_2 \, \hat{e}_2 + h_3 \, dq_3 \, \hat{e}_3
\end{gather*}$$

該平行六面體的體積為三邊的純量三重積；由 (a-2) 三邊互相垂直、由【定義 3】三個 $\hat{e}_i$ 皆為單位向量，三重積退化為三邊長相乘：

$$\begin{gather*}
dV &=& \left| \left( h_1 \, dq_1 \, \hat{e}_1 \right)\cdot\left[ \left( h_2 \, dq_2 \, \hat{e}_2 \right)\times\left( h_3 \, dq_3 \, \hat{e}_3 \right) \right] \right| \\
&\overset{\text{(a-2)}}{=}& h_1 h_2 h_3 \, dq_1 \, dq_2 \, dq_3 \\
&\overset{\text{(a-1)}}{=}& \left( 1 \right)\left( r \right)\left( r\sin\theta \right) dr \, d\theta \, d\phi \\
&=& r^2 \sin\theta \, dr \, d\theta \, d\phi
\end{gather*}$$

### (c) proof 梯度算子 (Gradient operator)

把梯度依正交基底展開為 $\nabla f = \sum_i \left( \nabla f \right)_i \hat{e}_i$，代入【已知 2】：

$$\begin{gather*}
df &\overset{\text{已知 2}}{=}& \nabla f \cdot d\vec{r} \\
&\overset{\text{(b)}}{=}& \left[ \sum_i \left( \nabla f \right)_i \hat{e}_i \right] \cdot \left[ \sum_j h_j \, dq_j \, \hat{e}_j \right] \\
&\overset{\text{(a-2)}}{=}& \sum_i \left( \nabla f \right)_i h_i \, dq_i
\end{gather*}$$

另一方面，純量場的全微分本身為

$$df = \sum_i \frac{\partial f}{\partial q_i}dq_i$$

三個 $dq_i$ 彼此獨立，故上下兩式中每一個 $dq_i$ 的係數必須各自相等：

$$\begin{gather*}
\left( \nabla f \right)_i h_i &=& \frac{\partial f}{\partial q_i} \\
\left( \nabla f \right)_i &=& \frac{1}{h_i}\frac{\partial f}{\partial q_i}
\end{gather*}$$

代入 (a-1) 的三個尺度因子：

$$\nabla f = \frac{\partial f}{\partial r}\hat{e}_r + \frac{1}{r}\frac{\partial f}{\partial \theta}\hat{e}_\theta + \frac{1}{r\sin\theta}\frac{\partial f}{\partial \phi}\hat{e}_\phi$$

### (d) proof 散度算子 (Divergence operator)

取一個三邊分別為 $h_1dq_1$、$h_2dq_2$、$h_3dq_3$ 的微小曲線盒子。垂直於 $\hat{e}_1$ 的兩個面，面積皆為 $h_2h_3 \, dq_2 \, dq_3$，其淨外向通量為

$$\begin{gather*}
d\Phi_1 &=& \left[ A_1 h_2 h_3 \right]_{q_1 + dq_1} dq_2 \, dq_3 - \left[ A_1 h_2 h_3 \right]_{q_1} dq_2 \, dq_3 \\
&=& \frac{\partial}{\partial q_1}\left[ A_1 h_2 h_3 \right] dq_1 \, dq_2 \, dq_3
\end{gather*}$$

另兩對面同理（下標輪換）。由【已知 3】，三個方向的淨通量相加再除以 (b) 的體積 $\Delta V = h_1h_2h_3 \, dq_1 \, dq_2 \, dq_3$：

$$\begin{gather*}
\nabla \cdot \vec{A} &\overset{\text{已知 3}}{=}& \frac{d\Phi_1 + d\Phi_2 + d\Phi_3}{\Delta V} \\
&\overset{\text{(b)}}{=}& \frac{1}{h_1 h_2 h_3}\left\{ \frac{\partial}{\partial q_1}\left[ A_1 h_2 h_3 \right] + \frac{\partial}{\partial q_2}\left[ A_2 h_3 h_1 \right] + \frac{\partial}{\partial q_3}\left[ A_3 h_1 h_2 \right] \right\} \\
&\overset{\text{(a-1)}}{=}& \frac{1}{r^2 \sin\theta}\left\{ \frac{\partial}{\partial r}\left[ A_r \, r^2 \sin\theta \right] + \frac{\partial}{\partial \theta}\left[ A_\theta \, r\sin\theta \right] + \frac{\partial}{\partial \phi}\left[ A_\phi \, r \right] \right\} \\
&=& \frac{1}{r^2}\frac{\partial}{\partial r}\left[ r^2 A_r \right] + \frac{1}{r\sin\theta}\frac{\partial}{\partial \theta}\left[ \sin\theta \, A_\theta \right] + \frac{1}{r\sin\theta}\frac{\partial A_\phi}{\partial \phi}
\end{gather*}$$

（最後一步中，$\sin\theta$ 對 $r$ 而言、$r$ 對 $\theta$ 與 $\phi$ 而言皆為常數，故可各自搬到微分之外，與前置的 $\dfrac{1}{r^2\sin\theta}$ 相消。）

### (e) proof 拉普拉斯算子 (Laplacian operator)

由【已知 4】，把 (c) 的梯度分量當成 (d) 的向量場分量，即令 $A_i = \dfrac{1}{h_i}\dfrac{\partial f}{\partial q_i}$：

$$\begin{gather*}
\nabla^2 f &\overset{\text{已知 4}}{=}& \nabla \cdot \left( \nabla f \right) \\
&\overset{\text{(c)(d)}}{=}& \frac{1}{r^2}\frac{\partial}{\partial r}\left[ r^2 \frac{\partial f}{\partial r} \right] + \frac{1}{r\sin\theta}\frac{\partial}{\partial \theta}\left[ \sin\theta \cdot \frac{1}{r}\frac{\partial f}{\partial \theta} \right] + \frac{1}{r\sin\theta}\frac{\partial}{\partial \phi}\left[ \frac{1}{r\sin\theta}\frac{\partial f}{\partial \phi} \right] \\
&=& \frac{1}{r^2}\frac{\partial}{\partial r}\left[ r^2 \frac{\partial f}{\partial r} \right] + \frac{1}{r^2 \sin\theta}\frac{\partial}{\partial \theta}\left[ \sin\theta \frac{\partial f}{\partial \theta} \right] + \frac{1}{r^2 \sin^2\theta}\frac{\partial^2 f}{\partial \phi^2}
\end{gather*}$$

+++

## 幾何解釋

### 尺度因子就是「座標刻度換算成尺」的匯率

$r$ 本身已經是長度，走一格 $dr$ 就真的走了 $dr$ 公尺，所以 $h_r = 1$。$\theta$ 與 $\phi$ 則是角度，走一格角度實際走多遠取決於離軸多遠：沿 $\theta$ 走的是半徑為 $r$ 的大圓，弧長為 $r\,d\theta$，故 $h_\theta = r$；沿 $\phi$ 走的是投影到 $xy$ 平面後半徑為 $r\sin\theta$ 的小圓，弧長為 $r\sin\theta\,d\phi$，故 $h_\phi = r\sin\theta$。**尺度因子的全部物理內容就是這句話**，後面三個算子只是把這個匯率一路帶下去。

### 為什麼體積元素會多出 $r^2\sin\theta$

$dV = h_rh_\theta h_\phi\,dr\,d\theta\,d\phi$ 只是「長 × 寬 × 高」，而三個邊長各自乘了自己的匯率。因此在球座標做積分時，$r^2\sin\theta$ **不是可以省略的裝飾**，它是把 $(dr, d\theta, d\phi)$ 這個「純座標盒子」換算成真實體積的雅可比因子。在 $\theta \to 0$ 或 $\theta \to \pi$（南北極）時 $\sin\theta \to 0$，正對應到那裡的經線全部收攏成一點、實際體積趨近於零。

### $\nabla^2$ 的三項為什麼長得不對稱

在卡氏座標中 $\nabla^2 = \partial_x^2 + \partial_y^2 + \partial_z^2$ 三項完全對稱，是因為三個尺度因子都是 1。一旦 $h_\theta, h_\phi$ 隨位置改變，散度就必須先把「面積」$h_jh_k$ 乘進去、微分完再除掉「體積」$h_1h_2h_3$，於是 $r$ 項冒出 $\dfrac{1}{r^2}\partial_r\left[r^2\,\cdot\,\right]$、$\theta$ 項冒出 $\dfrac{1}{\sin\theta}\partial_\theta\left[\sin\theta\,\cdot\,\right]$。這兩個「先乘後除」的包裹正是曲面幾何留下的痕跡；也因此 $\phi$ 項最乾淨——$h_\phi$ 完全不依賴 $\phi$ 自己。

### 這份推導在氫原子問題裡負責什麼

庫侖位能 $U \propto 1/r$ 是**點對點**的作用力，天生球狀對稱。在卡氏座標中 $r = (x^2+y^2+z^2)^{1/2}$ 同時出現在根號裡與分母上，$x, y, z$ 被綁死在一起，無法做變數分離；換到球座標後位能只剩 $1/r$ 一個變數，而 $\nabla^2$ 的三項恰好可以逐一被剝離，這就是氫原子薛丁格方程式能夠有解析解的**唯一**理由。
