# 控制系統-目錄

:::{note}
這是根據葉廷仁教授在[清華大學公開課-控制系統一](https://ocw.nthu.edu.tw/ocw/index.php?page=course&cid=133&)上的內容，
詳細和更準確的內容可以去參閱他的公開影片。
:::
## Outlines
__Part I: 控制系統一__
* {ref}`介紹控制系統`
	* 開迴路控制系統與閉迴路控制系統
	* 定義變數 
	* 控制系統的主要目的    
* {ref}`數學基礎`
	* Laplace Transform and Inverse Laplace Transform
	* Impulse Response
	* Bounded-input Bounded-output Stability
	* Routh-Hurwitz Criterion
	* Frequency Response
	* Bode Plot
* {ref}`方塊圖(Block diagrams)` 
  	* The origins of the story
    * Rayleigh-Barnard Convection 
    * Lorenz 63 model I (solutions) 
    * Lorenz 63 model II (stability analysis)
* {ref}`動態系統建模(Modeling dynamic system)` 
	* The physical and mathematical background
	* Single Scale
	* Multi-scale interations
	* HW3: Lorenz 96 model (calculating the Layapynov exponent) (10%)
* {ref}`控制系統的時域分析` 
	* Introduction to Liouville equation
	* Jacobian Matrix and Determinant  
	* Connections between Liouville equation and ensemble forecasts
* {ref}`根軌跡圖(Root locus analysis)` 
	* Liouville equation as a function of initial state vs current state 
	* Solution to Liouville equation
	* Liouville equation in 1st-order ODE case
	* Liouville equation in Lorenz 63 model
	* Challengs of applying Liouville Equation to weather forecast
	* Liouville equation and Singular Value Decomposition
	* HW4: Derivation of Liouville equation + LE in 1st-order ODE and Lorenz 84 model (20%)
* {ref}`控制系統的頻域分析`
    * Direct Method
	* von Neumann method
	* Energy Method
	* Stability in Geophysical Fluid Dynamics (Shear instability and Eady problem)
* {ref}`控制系統的設計`
	* Generalized stability theorem
	* Modal vs non-modal systems
    * Reduced-dimension problems


![](pic/goodplant1.png)

__Part II: 控制系統與大氣科學__ 
* Week 11: __The predictability of a flow which possesses many scales of motions (Lorenz 1969)__
	* Key Lecture: Week 8	
* Week 12: __Stochastic Forcing of ENSO by the Intraseasonal Oscillation (Moore and Kleeman 1999)__
	* Key Lecture: Week 9
* Week 13: __Ensemble-based sensitivity analysis (Hakim and Torn 2008)__
	* Key Lecture: Week 9
* Week 14: __The Critical Role of Non-Normality in Partitioning Tropical and Extratropical Contributions to PNA Growth (Henderson et al. 2020)__
	* Key Lecture: Week 9
* Week 15: __Physically Interpretable Neural Networks for the Geosciences: Applications to Earth System Variability (Toms et al. 2020)__
	* Key Lecture: Week 10

```{tableofcontents}
```
