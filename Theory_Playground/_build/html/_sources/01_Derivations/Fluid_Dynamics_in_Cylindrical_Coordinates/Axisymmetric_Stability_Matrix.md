# Axisymmetric Stability Matrix ($AC - B^2$ 圓柱座標證明)

+++


## 證明目標:

證明在圓柱座標系 $(r,\lambda,z)$ 穩定度的表達：

$$\det(\mathbf{S}_{\text{cyl}}) = \rho^2 (AC - B^2)$$

+++

## 假設與已知 (Assumptions & Preliminaries)


* **【假設 1】 軸對稱假設與背景場 (Axisymmetric & Background State Assumption)：**
  
    $$\frac{\partial}{\partial\lambda} = 0 \quad ,\quad \begin{cases} v_e(r,z) = \overline{v}(r,z) \\ b_e(r,z) = \overline{b}(r,z) \end{cases}$$

    * 系統在切線方向（方位角 $\lambda$）上沒有變化，這是一個成熟熱帶氣旋的標準假設。
    * 背景環境大氣（下標 $e$ 表示 environment）存在穩定且軸對稱的切線風場 $\overline{v}$ 和背景浮力 $\overline{b}$。

* **【定義 1】 浮力 (Buoyancy) 的簡化代換：**
    為了公式推導的簡潔，我們將含有重力加速度與參考位溫的項統一定義為浮力 $b$：

    $$b \overset{\text{def}}{=} \frac{g}{\theta_0}\theta$$

* **【定義 2】 絕對角動量 (Absolute Angular Momentum, $M$)：**
    單位質量的空氣塊不僅有相對於地球的旋轉角動量，還包含了隨地球自轉的角動量。

    $$M(r,z) \overset{\text{def}}{=} r\overline{v}(r,z) + \frac{1}{2}fr^2$$

    * 對 $r$ 偏微分：$\frac{\partial M}{\partial r} = \overline{v} + r\frac{\partial\overline{v}}{\partial r} + fr = r\left(f + \frac{\overline{v}}{r} + \frac{\partial\overline{v}}{\partial r}\right) = r(f+\zeta)$
    * 對 $z$ 偏微分：$\frac{\partial M}{\partial z} = r\frac{\partial\overline{v}}{\partial z}$

* **【已知 1】 [次環流結構參數 (Eliassen Coefficients)](https://derek1403.github.io/Theory_Playground/_build/html/01_Derivations/Fluid_Dynamics_in_Cylindrical_Coordinates/Eliassen_Secondary_Circulation_Coefficients.html)：**
    基於【假設 1】、【定義 1】，我們可以用 **背景浮力** $\overline{b}$ 與 **背景風場** $\overline{v}$ 重新表述結構參數：
    * 垂直穩定度： $A = \frac{\partial \overline{b}}{\partial z}$ 
    * 熱力風 / 斜壓性： $B = -\frac{\partial \overline{b}}{\partial r} = -\left(f+\frac{2\overline{v}}{r}\right)\frac{\partial \overline{v}}{\partial z}$
    * 慣性穩定度： $C = \left(f+\frac{2\overline{v}}{r}\right)(f+\zeta)$ 

* **【已知 2】 [梯度風平衡 (Gradient Wind Balance)](https://derek1403.github.io/Theory_Playground/_build/html/01_Derivations/Fluid_Dynamics_in_Cylindrical_Coordinates/Gradient_Wind_Balance.html)：**
    空氣塊在徑向受到的合力為零（離心力 + 科氏力 = 氣壓梯度力）

    $$\frac{v^2}{r} + fv = \frac{\partial\phi}{\partial r}$$

    * 對於起始位置的環境場：$\frac{v_e^2(r_0,z_0)}{r_0} + fv_e(r_0,z_0) = \frac{\partial\phi(r_0,z_0)}{\partial r} = F_{\text{PGF}}(r_0,z_0)$

* **【假設 2】 微小位移近似 (Small Displacement Approximation)：**
    質點移動的距離遠小於其所在半徑（$\delta r \ll r_0$），因此在分母的幾何項可做一階近似：

    $$\frac{1}{r_0+\delta r} \approx \frac{1}{r_0}$$

* **【假設 3】 質點守恆特性 (Parcel Theory)：**
    假設一個空氣質點（下標 $p$ 表示 parcel）在極短時間內被推離平衡位置 $(r_0, z_0)$，移動了微小位移 $(\delta r, \delta z)$ 到達新位置。質點在過程中**完全守恆**它出發時的絕對角動量與浮力：
    * $M_p(r_0+\delta r, z_0+ \delta z) = M_p(r_0, z_0) = M_e(r_0, z_0)$
    * $b_p(r_0+\delta r, z_0+ \delta z) = b_p(r_0, z_0) = b_e(r_0, z_0)$

* **【假設 4】 新位置的速度與環境速度皆十分接近原始出發點的環境速度：**
    
    $$v_p + v_e \approx 2\overline{v}(r_0,z_0)$$
  
* **【已知 3】 將速度改寫為絕對角動量：**
    
    $$\begin{gather*}
    v(r,z) &\overset{\text{定義 2}}{=}&\frac{M(r,z)}{r} - \frac{1}{2}fr \\
    v_p(r_0+\delta r,z_0+\delta z) - v_e(r_0+\delta r,z_0+\delta z) &=& \left( \frac{M_p(r_0+\delta r,z_0+\delta z)}{r_0+\delta r} - \frac{1}{2}f(r_0+\delta r) \right) - \left( \frac{M_e(r_0+\delta r,z_0+\delta z)}{r_0+\delta r} - \frac{1}{2}f(r_0+\delta r) \right) \\
    &=& \frac{M_p(r_0+\delta r,z_0+\delta z) - M_e(r_0+\delta r,z_0+\delta z)}{r_0+\delta r} \\
    &\overset{\text{假設 2}}{\approx}& \frac{1}{r_0} \left[ M_p(r_0+\delta r,z_0+\delta z) - M_e(r_0+\delta r,z_0+\delta z) \right] \\
    &\overset{\text{假設 3}}{=}& \frac{1}{r_0} \left[ M_e(r_0,z_0) - M_e(r_0+\delta r,z_0+\delta z) \right]
    \end{gather*}$$


* **【已知 4】 環境場的一階泰勒展開 (First-order Taylor Expansion for Environment)：**
    質點來到新位置 $(r_0+\delta r, z_0+\delta z)$ 時，周遭環境場的絕對角動量與浮力可近似為平衡位置的值加上微小變化：
    * $M_e(r_0+\delta r, z_0+ \delta z) \approx M_e(r_0, z_0) + \frac{\partial M(r_0,z_0)}{\partial r}\delta r + \frac{\partial M(r_0,z_0)}{\partial z}\delta z$
    * $b_e(r_0+\delta r, z_0+ \delta z) \approx b_e(r_0, z_0) + \frac{\partial b_e(r_0,z_0)}{\partial r}\delta r + \frac{\partial b_e(r_0,z_0)}{\partial z}\delta z$



+++


## 證明

這個證明的核心思維是尋找「擾動後的淨力（回復力）」。我們先處理水平方向（徑向）的加速度，再處理垂直方向的加速度，最後將它們寫成矩陣形式。

### 1. 徑向加速度 $\ddot{\delta r}$ (慣性與離心回復力)

質點的徑向加速度 $\ddot{\delta r}$ 來自於質點自身向外的力（離心力＋科氏力），減去新位置環境給予的向內氣壓梯度力 $F_{\text{PGF}}$。

$$\begin{gather*}
\ddot{\delta r} &=& F_{\text{outward, parcel}} - F_{\text{inward, env}} \\
&\overset{\text{已知 2}}{=}& \left( \frac{v_p^2(r_0+\delta r,z_0+\delta z)}{r_0+\delta r} + fv_p(r_0+\delta r,z_0+\delta z) \right) - F_{\text{PGF}}(r_0+\delta r,z_0+\delta z) \\
&\overset{\text{已知 2}}{=}& \left( \frac{v_p^2(r_0+\delta r,z_0+\delta z)}{r_0+\delta r} + fv_p(r_0+\delta r,z_0+\delta z) \right) - \left( \frac{v_e^2(r_0+\delta r,z_0+\delta z)}{r_0+\delta r} + fv_e(r_0+\delta r,z_0+\delta z) \right) \\
&\overset{\text{假設 2}}{\approx}& \left( \frac{v_p^2(r_0+\delta r,z_0+\delta z)}{r_0} + fv_p(r_0+\delta r,z_0+\delta z) \right) - \left( \frac{v_e^2(r_0+\delta r,z_0+\delta z)}{r_0} + fv_e(r_0+\delta r,z_0+\delta z) \right) \\
&=& \frac{1}{r_0}\left[ v_p^2(r_0+\delta r,z_0+\delta z) - v_e^2(r_0+\delta r,z_0+\delta z) \right] + f\left[ v_p(r_0+\delta r,z_0+\delta z) - v_e(r_0+\delta r,z_0+\delta z) \right] \\
&=& \frac{1}{r_0}\left[ v_p(r_0+\delta r,z_0+\delta z) + v_e(r_0+\delta r,z_0+\delta z) \right]\left[ v_p(r_0+\delta r,z_0+\delta z) - v_e(r_0+\delta r,z_0+\delta z) \right] \\
&& + f\left[ v_p(r_0+\delta r,z_0+\delta z) - v_e(r_0+\delta r,z_0+\delta z) \right] \\
&=& \left( \frac{v_p(r_0+\delta r,z_0+\delta z) + v_e(r_0+\delta r,z_0+\delta z)}{r_0} + f \right) \left[ v_p(r_0+\delta r,z_0+\delta z) - v_e(r_0+\delta r,z_0+\delta z) \right]\\
&\overset{\text{假設 4}}{=}& \left( \frac{2\overline{v}(r_0,z_0)}{r_0} + f \right) \left[ v_p(r_0+\delta r,z_0+\delta z) - v_e(r_0+\delta r,z_0+\delta z) \right] \\
&\overset{\text{已知 3}}{=}& \left( \frac{2\overline{v}(r_0,z_0)}{r_0} + f \right) \frac{1}{r_0} \left[ M_e(r_0,z_0) - M_e(r_0+\delta r,z_0+\delta z) \right] \\
&\overset{\text{已知 4}}{=}& \left( \frac{2\overline{v}(r_0,z_0)}{r_0} + f \right) \frac{1}{r_0} \left[ M_e(r_0,z_0) - \left( M_e(r_0,z_0) + \frac{\partial M(r_0,z_0)}{\partial r}\delta r + \frac{\partial M(r_0,z_0)}{\partial z}\delta z \right) \right] \\
&=& - \frac{1}{r_0} \left( f + \frac{2\overline{v}(r_0,z_0)}{r_0} \right) \left[ \frac{\partial M(r_0,z_0)}{\partial r}\delta r + \frac{\partial M(r_0,z_0)}{\partial z}\delta z \right] \\
&\overset{\text{定義 2}}{=}& - \frac{1}{r_0} \left( f + \frac{2\overline{v}(r_0,z_0)}{r_0} \right) \left[ r_0(f+\zeta)\delta r + r_0\frac{\partial\overline{v}(r_0,z_0)}{\partial z}\delta z \right] \\
&=& - \left( f + \frac{2\overline{v}(r_0,z_0)}{r_0} \right)(f+\zeta)\delta r - \left( f + \frac{2\overline{v}(r_0,z_0)}{r_0} \right)\frac{\partial\overline{v}(r_0,z_0)}{\partial z}\delta z \\
&\overset{\text{已知 1}}{=}& -C\delta r + B\delta z
\end{gather*}$$

### 2. 垂直加速度 $\ddot{\delta z}$ (浮力回復力)

垂直方向的加速度純粹來自於質點與新環境的浮力差（阿基米德浮力）：

$$\begin{gather*}
\ddot{\delta z} &=& b_p(r_0+\delta r,z_0+\delta z) - b_e(r_0+\delta r,z_0+\delta z) \\
&\overset{\text{假設 3}}{=}& b_e(r_0,z_0) - b_e(r_0+\delta r,z_0+\delta z) \\
&\overset{\text{已知 4}}{=}& b_e(r_0,z_0) - \left( b_e(r_0,z_0) + \frac{\partial b_e(r_0,z_0)}{\partial r}\delta r + \frac{\partial b_e(r_0,z_0)}{\partial z}\delta z \right) \\
&=& - \frac{\partial b_e(r_0,z_0)}{\partial r}\delta r - \frac{\partial b_e(r_0,z_0)}{\partial z}\delta z \\
&\overset{\text{已知 1}}{=}& B\delta r - A\delta z
\end{gather*}$$

### 3. 矩陣化與行列式

將兩個方向的回復力聯立，可以寫成優雅的穩定度矩陣形式：

$$\begin{gather*}
&\frac{d^2}{dt^2} \begin{bmatrix} \delta r \\ \delta z \end{bmatrix} &=& \begin{bmatrix} -C & B \\ B & -A \end{bmatrix} &\begin{bmatrix} \delta r \\ \delta z \end{bmatrix} \\
&&=& -\begin{bmatrix} C & -B \\ -B & A \end{bmatrix} &\begin{bmatrix} \delta r \\ \delta z \end{bmatrix} \\
&&=& -\mathbf{S}_{\text{cyl}}& \begin{bmatrix} \delta r \\ \delta z \end{bmatrix} \\
\Rightarrow& \det(\mathbf{S}_{\text{cyl}}) &=& AC - (-B)(-B) &= AC - B^2
\end{gather*}$$

+++


---

## 💡 物理學家的浪漫：不變的幾何對稱性

透過直接在圓柱座標中推導，我們印證了一件非常浪漫的事：**不管是用直線座標系看鋒面，還是用極座標系看颱風，流體力學的「穩定度矩陣」結構是宇宙通用的！**

唯一隱藏在細節裡的魔鬼是，圓柱座標在計算水平回復力時，那項對速度的偏微分 $\frac{\partial F}{\partial v} = f + \frac{2\overline{v}}{r}$，自然而然地把「離心力造成的剛性（$\frac{2\overline{v}}{r}$）」給生出來了。

這個額外生出來的離心剛性，就是為什麼颱風的 $C$ 參數會比中緯度鋒面的 $C$ 參數大上好幾個數量級的原因。大自然用完全相同的數學矩陣（碗與馬鞍），透過換了一套座標系，就創造出了兩種截然不同的天氣系統！

+++

這是一個非常有深度的延伸思考！你精準地抓住了矩陣分析的核心，並且開始嘗試把數學的排列組合對應到真實的大自然中。

我們一步步來破解你的疑問，先從數學排列的迷思開始，接著想像你提到的極端情況，討論 $B$ 的正負號物理意義，最後我會幫你把大氣的狀態整理成一張系統性的表格。

### 一、 數學迷思：真的有 81 種情況嗎？

答案是：**沒有那麼多，只有 27 種基礎組合。**

在我們的系統中，獨立的環境變數只有三個：$A$（垂直穩定度）、$C$（慣性穩定度）、$B$（斜壓性 / 熱力風）。
這三個變數各自可以是正、零、負（3 種狀態），所以排列組合是 $3 \times 3 \times 3 = 27$ 種。

至於 $AC-B^2$ 的正負號，它是被 $A, B, C$ **決定出來的結果**，不能當作第四個獨立變數隨意組合。舉例來說，如果 $A>0$ 且 $C<0$，那麼 $AC$ 必定小於 0；此時無論 $B$ 是多少（$B^2$ 必定大於等於 0），$AC-B^2$ **永遠只能小於 0**，不可能存在 $AC-B^2 > 0$ 的情況。因此，實際上的物理狀態遠比 81 種少得多。

-----

### 二、 想像 $A<0$ , $C<0$ , $AC-B^2>0$ 的極端世界

這是一個非常精彩的特例！我們用特徵值（Eigenvalue）來推導一下這代表什麼意思：

我們的穩定度矩陣行列式（特徵值乘積）是：
$\lambda_1 \lambda_2 = AC - B^2 > 0$
這代表兩個特徵值**同號**（不是兩個都正，就是兩個都負）。

矩陣的跡（Trace，主對角線元素相加，等於特徵值相加）是：
$\lambda_1 + \lambda_2 = A + C$
因為已知 $A<0$ 且 $C<0$，所以 $\lambda_1 + \lambda_2 < 0$。

兩個數字相乘大於 0，相加小於 0，唯一的可能就是：**$\lambda_1 < 0$ 且 $\lambda_2 < 0$**。

  * **數學曲面**：這是一個**向下開口的橢圓拋物面（倒蓋的碗）**。
  * **💡 直觀比喻**：想像你把一顆彈珠精準地放在一座**異常陡峭、完全平滑的冰山尖頂**上。
  * **物理與天氣意義**：這被稱為**絕對不穩定 (Absolute Instability)**。大氣在垂直方向是頭重腳輕的（冷空氣在溫暖空氣正上方，$A<0$），水平方向的旋轉也是互相撕裂的（絕對渦度為負，$C<0$）。而且斜壓性 $B$ 相對較弱，沒有提供足夠的耦合牽制。在這個環境下，無論你把空氣塊往哪個方向推（上下、左右、斜向），它都會**沿著冰坡加速滾下去，呈現指數級別的劇烈噴發**。在真實大氣中，這種狀態極難維持，只要一出現，瞬間就會爆發極度暴力的三維亂流與對流混合，強行把大氣「攪拌」回中性狀態。

-----

### 三、 斜壓性 $B$ 是正很多或負很多，不影響天氣嗎？

**「系統會不會不穩定」只看 $B^2$（大小），但「天氣系統長什麼形狀」則看 $B$ 的正負號（方向）！**

  * **影響穩定度的是 $B^2$**：在判別式 $AC-B^2$ 中，$B$ 被平方了。這代表無論冷空氣在左邊還是右邊，只要「水平溫度梯度」夠大，系統用來維持穩定的「扣打」就會被大量消耗，使得矩陣更容易掉入小於 0 的馬鞍面（對稱不穩定）。
  * **影響形狀的是 $B$ 的正負**：特徵向量（Eigenvector）的方向是由 $B$ 決定的。特徵向量代表系統最容易滑動的「傾斜軌道」。
      * 如果 $B > 0$，傾斜軌道可能朝向右上方傾斜（例如颱風眼牆向外傾斜的上升氣流）。
      * 如果 $B < 0$，傾斜軌道就會朝向左上方傾斜。
      * **總結**：$B$ 的大小決定了暴風雨會不會發生，而 $B$ 的正負號決定了暴風雨是「往外斜著下」還是「往內斜著下」。

-----

### 四、 大氣穩定度矩陣狀態總表 (The Stability Matrix Taxonomy)

為了清晰，我們將 27 種組合收斂成最具代表性的物理情境。我們以 $A$ 和 $C$ 為主軸，並探討 $B$ 的介入如何改變結果。

*(註：符號 $+$ 代表大於 0，$-$ 代表小於 0，0 代表等於 0)*

| 垂直 ($A$) | 慣性 ($C$) | 斜壓性 ($B$) | 判別式 ($AC-B^2$) | 數學曲面特徵 | 物理狀態與大氣特徵 | 天氣系統範例 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| $+$ | $+$ | 弱 (小) | **$+$** | 向上開口的碗 ($\lambda_1>0, \lambda_2>0$) | **絕對穩定 (Symmetrically Stable)**<br>任何方向的擾動都會震盪回原位。 | 晴朗無雲的穩定天氣、強烈高壓中心。 |
| $+$ | $+$ | 強 (大) | **$-$** | 馬鞍面 ($\lambda_1>0, \lambda_2<0$) | **對稱不穩定 (Symmetric Instability, SI)**<br>垂直和水平都穩定，但有一條特定的「斜線通道」阻力極小，質點會沿斜線噴發。 | 鋒面系統的傾斜降雨帶、颱風的螺旋雨帶。 |
| $+$ | $+$ | 臨界 | **0** | 拋物柱面 (U型槽) | **中性邊界狀態**<br>沿某個斜面擾動時無回復力（隨波逐流）。 | SI 即將觸發或剛混合完畢的過渡區。 |
| $+$ | $-$ | 任何值 | **$-$** | 馬鞍面 ($\lambda_1>0, \lambda_2<0$) | **慣性不穩定主導 (Inertial Instability)**<br>$A$ 想拉回，但 $C$ 崩壞。質點主要在水平方向失控擴散。 | 赤道反氣旋邊緣、強烈高空噴流出口區右側的水平猛烈輻散。 |
| $-$ | $+$ | 任何值 | **$-$** | 馬鞍面 ($\lambda_1>0, \lambda_2<0$) | **靜力不穩定主導 (Static Instability)**<br>$C$ 想拉回，但 $A$ 崩壞。質點主要在垂直方向劇烈上升。 | 午後熱對流、雷陣雨、積雨雲。 |
| $-$ | $-$ | 弱 (小) | **$+$** | 向下開口的碗 ($\lambda_1<0, \lambda_2<0$) | **絕對不穩定 (Absolute Instability)**<br>垂直與水平彈簧雙雙斷裂。 | 極端罕見。可能短暫出現於強烈龍捲風內部或微爆流的核心破壞區。 |
| $-$ | $-$ | 強 (大) | **$-$** | 馬鞍面 (但兩軸皆偏負) | **強烈複合不穩定**<br>不僅垂直水平不穩定，熱力風還加劇了特定斜向的破壞力。 | 猛烈的颮線 (Squall line) 發展初期。 |
| 0 | 0 | 0 | **0** | 絕對平坦 | **絕對中性 (Absolute Neutral)**<br>沒有任何回復力或破壞力。 | 大氣均質且無風的理想死寂狀態。 |
| $+, 0, -$ | 0 或 0 | $B \neq 0$ | **$-$** | 馬鞍面 | **邊界崩壞狀態**<br>只要 $A$ 或 $C$ 其中一個是 0，加上只要有一點點 $B$，系統必定掉入不穩定。 | 大氣穩定度極度脆弱，一觸即發的暴風雨前兆。 |

透過這張表你可以發現，大氣科學家之所以這麼在乎 **$AC-B^2$**，就是因為它完美統整了三維空間中各種複雜的受力關係，用一個簡單的數字正負號，就宣判了天氣系統的生與死！

+++

## 相關資料

* [穩定度矩陣與雅可比行列式之關係證明 (Axisymmetric Stability Matrix and Jacobian Matrix )](https://derek1403.github.io/Theory_Playground/_build/html/01_Derivations/Fluid_Dynamics_in_Cylindrical_Coordinates/Axisymmetric_Stability_Matrix_and_Jacobian_Matrix.html)


+++
