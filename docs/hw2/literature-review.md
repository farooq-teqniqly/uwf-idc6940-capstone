# Literature Review: Coordinated Vehicle Dispatching and Charging Scheduling for Electric Ride-Hailing Fleets

**Paper Reviewed:** Ma, T.-Y., Connors, R. D., & Viti, F. (2024). Coordinated vehicle dispatching and charging scheduling for an electric ride-hailing fleet under charging congestion and dynamic prices. *Transportation Research Part C: Emerging Technologies*.

## Background/Motivation

The transition to electric vehicles (EVs) in ride-hailing fleets represents a critical response to climate change. The New York City Taxi and Limousine Commission (TLC) has committed to electrifying its entire fleet by 2030, aiming to reduce approximately 600,000 tons of CO₂ emissions annually (Taxi & Limousine Commission, 2022). However, this transition introduces substantial operational challenges that existing research has not adequately addressed.

Ma et al. (2024) identify three critical gaps: most prior studies assume constant energy prices and uncapacitated (unlimited capacity) charging stations (Al-Kanj et al., 2020; Shi et al., 2020). Existing models fail to explicitly account for vehicle queuing at charging stations, and previous approaches lack minimum charging duration constraints and do not optimize charging amounts based on remaining daily energy needs, leading to inefficient over-charging that reduces vehicle availability.

The significance of this research lies in its direct impact on the economic viability of electric ride-hailing operations. With limited fast-charging infrastructure and the need for multiple daily charging sessions, effective charging management becomes essential for profitability, given volatile customer demand and time-varying electricity prices.

## Methods Used

Ma et al. (2024) propose a sequential Mixed Integer Linear Programming (MILP) approach called "CongestionAware" that decomposes the problem into three models operating at different temporal scales.

**Model P1: Day-Ahead Charging Schedule Planning** operates on 30-minute decision epochs, minimizing total charging operational costs while anticipating vehicles' energy needs and waiting times. The model incorporates realistic constraints: minimum charging duration requirements, maximum state-of-charge thresholds, and charger capacity constraints.

**Model P2: Batch Vehicle Dispatch** handles real-time vehicle dispatching on one minute epochs, maximizing profit by matching idle vehicles with customers while respecting state of charge and maximum waiting time constraints.

**Model P3: Online Vehicle-to-Charger Assignment** determines optimal vehicle to charger assignments in real-time, minimizing total charging operational time while adapting the day ahead plan based on current system state.

A key innovation is the **reactive adaptation mechanism** that dynamically adjusts the day ahead plan throughout the day, maintaining a pool of vehicles needing to charge and implementing a smart partial recharge strategy that anticipates remaining daily energy needs. The authors implement a discrete event simulation framework integrating all three models. The methodology explicitly models stochastic customer demand, charging congestion dynamics, and time-varying energy prices-factors that previous studies have simplified or ignored.

## Significance of the Work

Using realistic NYC yellow taxi data with 100 electric vehicles, the CongestionAware policy outperformed four benchmark approaches. For scenarios with 3,000 customers per day, the policy increased total profit by 7.65% to 10.69% and improved service rates by 7% to 10.8%. For scenarios with 4,000 customers per day, profit increased by 8.76% to 15.05%, and service rates improved by 7.9% to 12.3%. These gains were achieved through significant reductions in charging waiting times and more efficient charging operations.

The work makes several important contributions: it introduces realistic charging operation modeling including minimum charging duration constraints, maximum waiting time limits, and explicit queuing dynamics; it demonstrates the value of anticipating vehicles' energy needs rather than using simple threshold-based policies; and it shows that partial recharge strategies significantly improve system performance. The results demonstrate that effective charging management can substantially improve profitability and service quality for transport network companies.

## Connection to Other Work

Ma et al. (2024) build upon optimization-based and reinforcement learning approaches. They reference model predictive control approaches (Zhang et al., 2016; Iacobucci et al., 2019) but note these are limited to small problem sizes and assume uncapacitated charging stations. Their work extends sequential MILP approaches (Jamshidi et al., 2021; Zalesak & Samaranayake, 2021; Ma, 2021) by explicitly modeling charging queuing times and incorporating more realistic constraints.

The paper differs from earlier sequential MILP studies: Jamshidi et al. (2021) approximate waiting times without explicit queuing models; Zalesak and Samaranayake (2021) do not consider heterogeneous charging infrastructure or time-dependent energy prices; Ma (2021) assumes linear charging speeds and homogeneous infrastructure. The authors also situate their work relative to reinforcement learning approaches (Al-Kanj et al., 2020; Yan et al., 2023; Kullman et al., 2021; Ahadi et al., 2022), noting that RL methods often assume uncapacitated charging stations and full-recharge policies. This work distinguishes itself through comprehensive treatment of realistic charging constraints.

## Relevance to Capstone Project

This paper is highly relevant to my capstone project, which extends my previous time-series forecasting work on Uber trip durations (using ARIMA models) by incorporating machine learning-based prediction methods and comparing their performance. My capstone will use Uber ride-sharing data from NYC TLC to develop both time-series forecasting and ML-based prediction models, then compare their accuracy. While the paper focuses on charging management, it provides methodological insights for trip duration prediction.

The paper's treatment of stochastic customer demand directly relates to understanding trip duration patterns. The authors use NYC yellow taxi data and demonstrate how demand volatility affects vehicle operations—insights crucial for predicting trip durations. While the paper uses yellow taxi data, my capstone will use Uber ride-sharing data from NYC TLC. The day-ahead planning approach that anticipates energy consumption based on historical patterns parallels the need to predict trip durations using both time-series and ML methods.

The paper's emphasis on anticipating future needs based on historical patterns aligns with time-series forecasting methods, while its consideration of multiple factors suggests ML models could capture complex non-linear relationships. My capstone focuses on developing and evaluating both time-series forecasting models (extending my previous ARIMA work) and ML-based prediction models, then comparing their performance. While accurate trip duration predictions could benefit charging optimization frameworks in future work, that integration is outside my capstone scope.

## Conclusion

Ma et al. (2024) present a comprehensive approach to coordinated vehicle dispatching and charging scheduling for electric ride-hailing fleets. The work addresses significant gaps by explicitly modeling charging congestion, incorporating realistic constraints, and developing an anticipative planning framework with reactive adaptation. The substantial performance improvements (up to 15% profit increase and 19% service rate improvement) validate the importance of sophisticated charging management.

For my capstone project comparing time-series forecasting and ML-based prediction methods for trip duration using Uber ride-sharing data from NYC TLC, this paper provides valuable insights into temporal patterns, demand forecasting, and the challenges of modeling stochastic demand in ride-hailing systems. The paper's approach to anticipating future needs based on historical patterns and multiple factors aligns with both time-series and ML methodologies. My capstone focuses on extending my previous ARIMA work with ML-based prediction methods and comparing their performance.

## References

Ahadi, R., Ketter, W., Collins, J., & Daina, N. (2023). Cooperative learning for smart charging of shared autonomous vehicle fleets. *Transportation Science*, 57(3), 613-630. https://doi.org/10.1287/trsc.2022.1187

Al-Kanj, L., Nascimento, J., & Powell, W. B. (2020). Approximate dynamic programming for planning a ride-hailing system using autonomous fleets of electric vehicles. *European Journal of Operational Research*, 284(3), 1088-1106. https://doi.org/10.1016/j.ejor.2020.01.033

Iacobucci, R., McLellan, B., & Tezuka, T. (2019). Optimization of shared autonomous electric vehicles operations with charge scheduling and vehicle-to-grid. *Transportation Research Part C: Emerging Technologies*, 100, 34-52. https://doi.org/10.1016/j.trc.2019.01.011

Jamshidi, H., Correia, G. H. A., van Essen, J. T., & Nökel, K. (2021). Dynamic planning for simultaneous recharging and relocation of shared electric taxis: A sequential MILP approach. *Transportation Research Part C: Emerging Technologies*, 125, 102933. https://doi.org/10.1016/j.trc.2020.102933

Kullman, N. D., Cousineau, M., Goodson, J. C., & Mendoza, J. E. (2021). Dynamic ride-hailing with electric vehicles. *Transportation Science*, 56(3), 775-794. https://doi.org/10.1287/trsc.2021.1042

Laha, A., Yin, B., Cheng, Y., Cai, L. X., & Wang, Y. (2019). Game theory based charging solution for networked electric vehicles: A location-aware approach. *IEEE Transactions on Vehicular Technology*, 68(7), 6352-6364. https://doi.org/10.1109/TVT.2019.2916475

Ma, T.-Y. (2021). Two-stage battery recharge scheduling and vehicle-charger assignment policy for dynamic dial-a-ride services. *PLoS One*, 16(5), e0251582. https://doi.org/10.1371/journal.pone.0251582

Ma, T.-Y., Connors, R. D., & Viti, F. (2024). Coordinated vehicle dispatching and charging scheduling for an electric ride-hailing fleet under charging congestion and dynamic prices. *Transportation Research Part C: Emerging Technologies*.

Maljkovic, M., Nilsson, G., & Geroliminis, N. (2023). Hierarchical pricing game for balancing the charging of ride-hailing electric fleets. *IEEE Transactions on Control Systems Technology*, 31(6), 2728-2743. https://doi.org/10.1109/TCST.2023.3286330

Shi, J., Gao, Y., Wang, W., Yu, N., & Ioannou, P. A. (2020). Operating electric vehicle fleet for ride-hailing services with reinforcement learning. *IEEE Transactions on Intelligent Transportation Systems*, 21(11), 4822-4834. https://doi.org/10.1109/TITS.2019.2947408

Taxi & Limousine Commission. (2022). CHARGED UP! TLC's roadmap to electrifying the for-hire transportation sector in New York City.

Yan, P., Yu, K., Chao, X., & Chen, Z. (2023). An online reinforcement learning approach to charging and order-dispatching optimization for an e-hailing electric vehicle fleet. *European Journal of Operational Research*, 310(3), 1218-1233. https://doi.org/10.1016/j.ejor.2023.03.039

Zalesak, M., & Samaranayake, S. (2021). Real time operation of high-capacity electric vehicle ridesharing fleets. *Transportation Research Part C: Emerging Technologies*, 133, 103413. https://doi.org/10.1016/j.trc.2021.103413

Zhang, R., Rossi, F., & Pavone, M. (2016). Model predictive control of autonomous mobility-on-demand systems. In *2016 IEEE International Conference on Robotics and Automation (ICRA)* (pp. 1382-1389). IEEE. https://doi.org/10.1109/ICRA.2016.7487272
