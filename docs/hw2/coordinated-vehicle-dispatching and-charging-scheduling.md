Coordinated vehicle dispatching and charging scheduling for an electric ride-hailing fleet
under charging congestion and dynamic prices

Tai-Yu Ma*, Luxembourg Institute of Socio-Economic Research (LISER), 11 Porte des Sciences, 4366 Esch-
sur-Alzette, Luxembourg
Richard  D.  Connors,  Luxembourg  Institute  of  Science  and  Technology  (LIST),  5  Avenue  des  Hauts-
Fourneaux, 4362 Esch-sur-Alzette, Luxembourg
Francesco VIti, Department of Engineering, University of Luxembourg, Esch-sur-Alzette, Luxembourg

Abstract

Effective utilization of charging station capacity plays an important role in enhancing the profitability of
ride-hailing  systems  using  electric  vehicles.  Existing  studies  assume  constant  energy  prices  and
uncapacitated  charging  stations  or  do  not  explicitly  consider  vehicle  queueing  at  charging  stations,
resulting  in  over-optimistic  charging  infrastructure  utilization.  In  this  study,  we  develop  a  dynamic
charging  scheduling  method  (named  CongestionAware)  that  anticipates  vehicles’  energy  needs  and
coordinates their charging operations with real-time energy prices to avoid long waiting time at charging
stations and increase the total profit of the system. A sequential mixed integer linear programming model
is proposed to devise vehicles’ day-ahead charging plans based on their experienced charging waiting
times and energy consumption. The obtained charging plans are adapted within the day in response to
vehicles’ energy needs and charging station congestion. The developed charging policy is tested using
NYC yellow taxi data in a Manhattan-like study area with a fleet size of 100 vehicles given the scenarios
of 3000 and 4000 customers per day. The computational results show that our CongestionAware policy
outperforms different benchmark policies with up to +15.06% profit and +19.16% service rate for 4000
customers per day. Sensitivity analysis is conducted with different system parameters and managerial
insights are discussed.

Keywords: ride-hailing, electric vehicle, dynamic charging management, capacitated charging network,
time-of-use energy prices, optimization

1. Introduction

The climate change crisis has motivated governments and Transport Network Companies to accelerate
fleet electrification to reduce CO2 emissions. Charging management is becoming a significant issue for
deploying this clean air transition policy due to the long charging times of electric vehicles (EVs) compared
to refueling internal combustion engine vehicles. According to a recent TLC Electrification Report (Taxi &
Limousine  Commission,  2022),  TLC  plans  to  transform  its  licensed  fleet  to  EVs  by  2030  to  reduce
environmental impact (around 600k tons of CO2 in 2022). However, due to the high investment costs of
rapid chargers, only a limited number of fast charging stations are available in major cities in the United
States. Furthermore, the high daily mileage of TLC’s vehicles necessitates drivers to charge their vehicles
several times a day, relying mainly on rapid chargers to save charging time (Jenn, 2019). Optimizing the
utilization  of  limited  fast-charging  resources  in  a  stochastic  environment  has  become  a  significant
challenge for this EV transition.

Several factors make dynamic charging management of electric ride-hailing systems challenging. First,
customer  demand  is  volatile,  affecting  vehicles’  charging  needs  over  time.  Second,  rapid  chargers
(charging power 50kWh) are limited due to their high investment costs. This might result in EVs queuing
at  charging  stations,  thereby  increasing  charging  station  search  costs  for  the  drivers.  Furthermore,
charging costs might vary according to the time of day due to variations in electricity prices. The decision
on  when  and  how  much  energy  to  recharge  becomes  a  significant  online  decision  problem  for

1

drivers/fleet operators to maximize their profit. However, most studies assume constant energy prices
and neglect congestion issues at charging stations (Al-Kanj et al., 2020; Shi et al., 2020).

Methodologies  developed  in  recent  years  are  mainly  based  on  mixed  integer  programming
optimization approaches, where the problem is decomposed into sequential sub-problems over different
planning horizons for vehicle dispatching, relocation, and charging scheduling to respond to uncertain
customer demand. In the first stage, a long-time horizon planning model is used to determine how many
vehicles to charge and at what type of chargers for each decision time interval (typically half an hour) for
the day by anticipating vehicles’ energy demand. The objective is to determine vehicles’ charging times
and durations for the day to minimize a desired objective function (e.g. minimize the number of total
charging trips and rejected customers (Jamshidi et al., 2021) or the shortage of available vehicles (Zalesak
and Samaranayake, 2021) or total charging operational costs (Ma, 2021) for the planning horizon. In the
second stage, a short-time horizon planning model is applied to determine where to charge to minimize
total  charging  access  costs  or  charging  operational  costs  (including  access  times,  waiting  times,  and
charging durations) under the capacity constraints of charging stations. Three drawbacks can be identified
in these existing works. First, when vehicles wait to charge at charging stations, there are no maximum
waiting time limits, resulting in unrealistically long waiting times at charging stations. Second, there is no
minimum charging duration constraint per each charging operation, which might result in undesirably
short charging durations (damaging battery lifespan) and inefficient charging operations (requiring higher
charging access times/costs and setup times due to more frequent charging operations). Third, vehicles
only need enough energy to reach the end of their working day, when overnight charging is available;
ignoring  this  results  in  more  charging  than  is  needed.  Consequently,  vehicles  might  charge  longer,
resulting in a shortage of available vehicles to serve customers.

This study aims to address the aforementioned drawbacks of existing studies for efficient charging
management  of  dynamic  ride-hailing  systems  under  stochastic  demand  with  more  realistic  charging
operation modeling. The main contributions of this study are summarized as follows.
a)  We propose a novel sequential mixed integer linear programming (MILP) approach to jointly optimize
vehicle  dispatch  and  charging  operations  to  maximize  the  profit  of  ride-hailing  systems  under
stochastic demand. The model first devises a day-ahead charging plan by anticipating vehicle waiting
times  at  different  chargers  and  vehicle  energy  consumption  for  the  day.  As  customer  demand  is
stochastic,  a  novel  reactive  model  is  proposed  to  adapt  the  current  system  state  and  anticipate
vehicles’ waiting times at charging stations. The remaining energy needs for the day are anticipated,
and vehicle charging time, duration, and where to charge are optimized online. Our computational
study  shows  that  the  proposed  charging  policy  significantly  increases  customer  service  rate  and
operators’ profit by reducing vehicles’ waiting times and charging durations at charging stations.
b)  Existing studies are based on simplified models for vehicle charging and waiting time estimation. This
study considers more realistic charging operation modeling and simulation under congested charging
facilities, including minimum charging time requirements and maximum queueing time when waiting
for  charging.  Moreover,  more  flexible  energy  prices  are  considered  (real-time  or  charging-type-
specific), allowing testing the performance of the proposed methodology under different dimensions
of uncertainty (demand, charging waiting time, queuing, and energy prices).

c)  Numerical  experiments  are  conducted  using  realistic  NYC  yellow  taxi  data,  and  the  impacts  of
different  system  parameters  (battery  capacity,  maximum  waiting  times  at  chargers,  number  of
chargers, and customer demand variability) are analyzed. The performance of the proposed approach
is compared  with several benchmark charging policies,  showing its  benefit  in increasing  customer
service rate and total profit of the operator in a stochastic environment.

The organization of this paper is as follows. We first present the related studies. Section 3 presents
the problem description, developed models and benchmark charging policies. Section 4 describes the test
instances and reports the computational studies. The impact of different system parameters is analyzed.
Finally, the conclusion is drawn, and future extensions are discussed.

2

2. Related studies

Dynamic  charging  management  of  ride-hailing  systems  involves  sequential  decision  making  under
uncertainty. Recent works for addressing this problem are mainly based on optimization-based approach
and reinforcement  learning (RL). Earlier  studies can be  classified into two categories of methodology:
sequential mixed integer programming approaches and RL. As it is not possible to jointly optimize all the
decision  variables  (vehicle  dispatching  and  charging)  under  uncertainty  and  system  dynamics,  the
problem  can  be  approximated  as  a  sequential  decision  making  problem  based  on  a  decomposition
approach. The sequential mixed integer programming approach is based on this optimization framework.
This  approach  decomposes  the  dynamic  charging  scheduling  problem  into  multiple  decision  horizons
where the long horizon planning for the day to determine  the number of vehicles to charge, charging
time, and durations for each charging decision time interval (e.g. half an hour). In contrast, short-horizon
planning  aims  to  determine  where  to  charge,  given the  charging  plans  obtained  at  the  first  step.  The
second approach (RL) considers dynamic vehicle dispatching, relocation, and charging management as
sequential decision-making problems under uncertainty and models the problem as a Markov decision
process.  Under  the  RL  framework,  the  operator  is  considered  as  an  agent  making  these  decisions  to
maximize the total profit of the system. Recent studies extend the single-agent-based approach to the
multi-agent-based approach to allow individual vehicles to make their own decisions in response to local
information of the system. More detailed reviews are described as follows.

Optimization-based  approaches:  Earlier  works  on  dynamic  ride-hailing  systems  focus  on  vehicle
dispatching  and  relocation  optimization  under  stochastic  demand.  Vehicle  charging  operations  are
simplified  by  assuming  uncapacitated  charging  stations  or  simply  neglected  by  considering  internal
combustion engine vehicles. Existing methodology can be classified into four categories as follows.

Model predictive control
This approach uses a model to represent the system dynamics based on which a set of control variables
is optimized to minimize a cost function over a prediction horizon. The process is repeated until the end
of the planning horizon. Zhang et al. (2016) proposed a model predictive control approach for operating
a dynamic ride-hailing system using autonomous vehicles. Vehicles’ charging scheduling problems are not
considered. Iacobucci et al. (2019) extended their work for the fleet management of shared autonomous
EVs based on the model predictive control approach. Two different model predictive control schemes
interact  over  different  planning  horizons:  one  for  vehicle  dispatching  and  relocation  decisions,  and
another for vehicle charging scheduling. However, the applicability of the developed approach is limited
to  small  problem  sizes  with  tens  of  vehicles,  and  charging  congestion  is  not  considered  by  assuming
uncapacitated charging stations.
Sequential mixed integer programming
This  approach  decomposes  the  system  dynamics  into  several  sub-processes  with  different  temporal
dimensions,  usually  embedded  in  a  hierarchical  structure.  Given  this  underlying  structure,  different
models are developed to pre-allocate limited resources or re-optimize the decision variables based on
the current system state or prediction of system changes over a prediction horizon. For example, Jamshidi
et al. (2021) proposed a three-stage sequential MILP model to address e-taxi dispatching, relocation, and
charging with charging station capacity constraints and time-of-use energy prices. However, waiting times
at charging stations are approximated without explicitly modeling charging queuing times on different
chargers. Zalesak and Samaranayake (2021) developed a MILP model to optimize the charging schedules
of  ride-pooling systems using EVs.  A two-stage  planning framework is  proposed: a long-time  planning
horizon  optimization  model  for  determining  when  to  charge  and  a  short-time  planning  horizon
optimization model to determine where to charge. The objective of the long-time horizon planning model
is to maintain a sufficient fleet size to meet varying customers’ demands and vehicles’ energy needs for
the planning horizon. The number of vehicles recharged for each decision time interval cannot exceed
the  capacity  of  total  charging  stations.  Heterogeneous  charging  infrastructure  and  time-dependent
energy  prices  are  not  considered.  For  the  short-time  horizon  planning,  a  simple  vehicle-to-charging-
station  assignment  model  is  formulated  to  minimize  vehicles’  total  charging  access  distance  under
3

charging station capacity constraints. Ma (2021) proposed a two-stage MILP model for dynamic charging
management of shared ride-hailing services. The developed approach anticipates vehicles’ driving needs
and waiting time at chargers to determine charging time and durations per half an hour to minimize total
daily charging operational costs. An online vehicle-to-charger assignment model is applied to minimize
total charging operational times under charging station capacity constraints. Several simplifications are
made for this study. First, the charging speed of vehicles is assumed linear without distinguishing the fact
that vehicles’ charging speed slows down when their state-of-charge (SoC) is above a threshold (around
80% of vehicles’ battery capacity). Note that SoC is measured in kWh. Second, the charging infrastructure
is homogeneous, and the minimum charging duration per charging operation is not considered. Yang et
al. (2019) proposed a two-stage charging coordination approach for optimizing electric taxi fleet charging
operations  by  considering  the  current  queuing  state  at  charging  stations.  The  first-stage  problem
determines when vehicles go to recharge using a time-dependent charging cost function that considers
average revenue loss per kWh charged. The second-stage problem determines where to recharge as a
Nash equilibrium problem to model non-cooperative taxi drivers’ charging station selections.
Optimization-embedded heuristics
This  approach  decomposes  the  sequential  decision  process  under  a  rolling  horizon  framework,  then
solves an optimization model iteratively until the end of the planning period. The considered optimization
problem  aims  to  jointly  optimize  idle  vehicle  relocation  and  charging  operations  to  minimize  a  cost
function under vehicle operations and charging capacity constraints. Pantelidis et al. (2022) developed a
MILP to optimize vehicle relocation and charging for electric carshare systems jointly. The optimization
problem is modeled as a route-capacitated minimum cost-flow relocation problem. A node-charge graph
is proposed to allow partial recharges over different discretized recharge levels to cover vehicle energy
needs  for  serving  customers.  A  simulation  case  study  is  conducted  using  realistic  carshare  data  in
Brooklyn. Yi and Smart (2021) proposed a heuristic for vehicle repositioning and charging management
of ride-hailing systems using autonomous EVs. Vehicles go to the nearest unoccupied charging stations
to recharge when their SoCs are below a predefined threshold. Dean et al. (2022) proposed a MILP model
to jointly optimize vehicle relocation and charging operations for shared autonomous EVs using zones as
the operational units. When assigning vehicles for charging in a zone, the number of vehicles for charging
cannot exceed the total charging station capacity. Vehicles' queuing times at charging stations are not
explicitly modeled.
Charging demand management using dynamic pricing
The above three approaches do not leverage dynamic pricing to mitigate charging congestion for better
utilization of limited charging facilities. Several studies integrate dynamic charging pricing to manage the
charging  demand  of  demand-responsive  mobility  systems  to  better  allocate  charging  resources  and
balance  charging  demand.  This  congestion  pricing  approach  has  been  widely  applied  for  road  traffic
management  and  charging  management  of  private  EVs  (Yu  and  Hong,  2017;  Zhang  et  al.,  2021).  For
shared mobility services, Maljkovic et al. (2023) propose a hierarchical control, game-theoretical based
mechanism  to  coordinate  the  charging  operations  of  multiple  ride-hailing  operators.  The  problem  is
formulated as a reverse Stackelberg game with a central authority (e.g., grid operator) at the upper level
(minimizing a cost function) and multiple ride-hailing operators at the lower level (maximizing their own
profits).  Assuming  different  charging  tariffs  on  different  charging  stations,  the  ride-hailing  operators
determine  their  vehicle-to-charging-station  assignment  to  minimize  the  charging  operation  costs  and
maximize the total profit. The central authority wants to balance the load over different charging stations
using  dynamic  pricing.  Given  the  non-cooperative  behavior  of  different  ride-hailing  operators,  system
optimal pricing policies under Nash equilibrium are searched. Another similar study is Laha et al. (2019),
who  developed  dynamic  pricing  strategies  for  charging  stations  to  maximize  their  own  utility  under
limited  charging  station  capacity,  considering  that  EV  users  select  their  charging  stations  based  on
charging prices and charging station location via real-time information sharing. The problem is modeled
as a multi-leader multi-follower Stackelberg game, and a dynamic pricing strategy is proposed to achieve
the Stackelberg equilibrium.

Reinforcement-learning-based  approaches:  RL  is  a  mode-free  approach  that  has  been  successfully
applied to solving various sequential decision-making problems under uncertainty (Farazi et al., 2021).
4

For  dynamic  ride-hailing  systems  using  EVs,  Al-Kanj  et  al.  (2020)  proposed  an  approximate  dynamic
programming approach for  ride-hailing  fleet management to maximize the  operators'  profit.  Vehicles’
dispatching, relocation, and charging decisions (actions) are controlled by a central controller. The system
state (vehicles’ locations, SoCs, activities, etc.) and time are discretized. Charging stations are assumed
uncapacitated and vehicles are fully recharged for each charging operation. As the possible state-action
combination  is  huge,  an  approximate  dynamic  programming  approach  is  applied  with  hierarchical
aggregation  for  value  function  approximation.  Yan  et  al.  (2023)  proposed  an  online  model-based  RL
algorithm based on  State–action–reward–state–action (SARSA)  for joint vehicle dispatch and charging
optimization of  electric  ride-hailing  systems.  Like  the  previous  study,  a  full-recharge  policy  is  applied.
Kullman et al. (2021) developed a deep reinforcement learning (DRL) approach to overcome the curses
of dimensionality for electric ride-hailing systems. A hybrid scheme is proposed where the problem of
vehicle dispatching is solved by a MILP optimization model, and vehicle relocation and charging decisions
are  made  under  the  RL  framework.  Unlike  the  single-agent-based  RL  approaches,  Ahadi  et  al.  (2022)
propose a multiagent-based DRL approach for the fleet management of shared and autonomous EVs. The
authors proposed a hierarchical learning and mean-field approximation approach to coordinate vehicles’
charging decisions under charging station capacity constraints to maximize the total revenue of the fleet.
A comprehensive review of RL-based approaches for EV charging management can be found in Abdullah
et al. (2021).

3. Dynamic charging management with charging congestion and real-time energy prices

In this section, we first present the problem description, then formulate the problem using mixed
integer linear programming, which includes three models: a) day-ahead charging planning, b)
vehicle  dispatching,  and  c)  online  vehicle-to-charger  assignment.  We  present  the  simulation
framework to test the proposed approach and compare its performance with four benchmark
charging approaches.

Notation
Parameter
𝑇
𝑇0
𝑢
𝑝ℎ
𝜆ℎ
𝐶
𝜑𝑠
𝜇
𝛾
𝛼𝑠

𝛽0, 𝛽1

𝐵𝑣
𝑚𝑖𝑛
𝐸𝑣
𝑚𝑎𝑥
𝐸𝑣

0
𝐸𝑣
𝐸̅𝑣

𝑚𝑎𝑥

𝑌𝑠

𝛿ℎ

Planning horizon (i.e., 24:00)
The starting time of service (i.e., 6:00 a.m.)
Type of chargers, 𝑢 ∈ 𝑈 = {fast, slow}
Average energy price in charging decision epoch ℎ (dollar/kWh)
The number of customers’ arrivals during charging decision epoch ℎ
Average travel cost for recharge per charging operation (dollar)
Charging power of charger 𝑠 (kW)
Energy consumption rate per kilometer traveled (kWh/km)
Average profit per minute traveled (dollar/km)
Minimum charging time per charging operation for the charger type for the
charger s
𝛽0 is the base rate and 𝛽1 is a distance-based operating fee (dollar/km) for a
service trip
Battery capacity of vehicle 𝑣 (KWh)
Minimum (reserve) SoC of vehicle 𝑣 (kWh)
Maximum threshold of SoC of vehicle 𝑣 with theoretical maximum charging
speed (kWh) (e.g. 80% of vehicle's battery capacity)
Initial SoC of vehicle 𝑣 for the charging schedule planning (KWh)
Planned battery level after recharge for vehicle 𝑣 at the end of charging decision
epoch ℎ (ℎ is dropped)
The maximum amount of energy that can be charged on charger 𝑠 during one
charging decision epoch (kWh)
Average energy consumption of a vehicle for charging decision epoch ℎ (kWh)

5

𝑡̅𝑣𝑠, 𝑡̅𝑣𝑜𝑟

𝑑̅𝑖𝑗
𝑊𝑟𝑡
𝑊𝑚𝑎𝑥
𝑊𝑣𝑠
𝑊̅ℎ𝑠

𝜋
𝜃

∆𝒷, ∆ℓ

𝑛𝐻ℓ

Set

𝐻𝒷

𝐻̂ℓ

𝐻ℓ

𝑅𝑡

𝑉
𝑉̃ℎ

𝑉𝑡
Ω𝑡
Ω̃𝑡
𝑆

Travel time from vehicle 𝑣’s current location to the location of charger 𝑠 or
customer 𝑟’s pickup location(minute)
Shortest path distance between location 𝑖 and 𝑗 (km)
Experienced wait time of request 𝑟 by the time 𝑡
Maximum waiting time of customers (same for each customer)
Waiting (queuing) time at charger 𝑠 for vehicle 𝑣 (ℎ is dropped)
Expected waiting time of vehicles when arriving at the charger 𝑠 at the beginning
of epoch ℎ
Cost per kilometer traveled of vehicles (dollar)
SoC threshold under which vehicles are added to the pool of go-charge vehicles
(% of vehicles’ battery capacity)

∆𝒷: batch dispatch decision time interval (e.g., 1 minute); ∆ℓ: charging schedule
planning decision time interval (e.g., 30 minutes)
The number of charging decision epochs for the planning horizon 𝑇, starting from
𝑇0 with the decision time interval ∆ℓ, i.e., 𝑛𝐻ℓ = ⌈
ceiling function returning the smallest integer greater than or equal to 𝑥.

⌉ where ⌈𝑥⌉ denotes the

𝑇−𝑇0
∆ℓ

Set of decision epochs for batch dispatch with the decision time interval ∆𝒷 (e.g.
1 minute), i.e., 𝐻𝒷 = {1,2, … , ⌈

⌉}

𝑇−𝑇0
∆𝒷

𝑇−𝑇0
∆ℓ

Set of decision epochs for charging schedule planning for the day with decision
time interval ∆ℓ, 𝐻̂ℓ = {1,2, … , ⌈
⌉}
Set of the shifted decision epochs for charging schedule planning, i.e.,  𝐻ℓ =
{1,2, … , 𝑛𝐻ℓ + 1} where the first index 1 in 𝐻ℓ denotes the first charging decision
epoch in 𝐻̂ℓ with SoC lower than 𝐸𝑣
𝑚𝑎𝑥 (80% of battery capacity as vehicles are
not to charge above this threshold to save charging times during service hours).
The end 𝑛𝐻ℓ + 1 corresponds to the end of the day.
Set of unserved requests (customers) at the beginning of batch dispatch time
index 𝑡
Set of vehicles
Sets of vehicles that need to recharge (𝑉̃ℎ) at time 𝑡 = ℎ∆ℓ (output of day-ahead
charging plan model)
Set of idles vehicles at time 𝑡 (online optimization)
Set of need-to-charge vehicles at time 𝑡 (online optimization)
Set of to-charge vehicles at time 𝑡 (online optimization)
Set of chargers

Variable

𝑡
ℎ
𝑠
𝑟
𝑒𝑣ℎ, 𝑒𝑣𝑡

𝑜𝑟, 𝑑𝑟

Index of batch dispatch epoch, 𝑡 ∈ 𝐻𝒷
Index of charging schedule planning decision epoch
Charger
Request (customer)
Battery level of vehicle 𝑣 at the beginning of epoch ℎ (charging schedule
planning) or epoch 𝑡 (customer batch dispatch)(Kilowatt-hour, kWh)
Pickup/drop-off location of request 𝑟

Decision variable
𝑣
𝑥ℎ𝑠
𝑣
𝑦ℎ𝑠
𝑥̂𝑣𝑠
𝑦̂𝑣𝑠

Indicator: 1 if vehicle 𝑣 is assigned to charger 𝑠 in epoch ℎ, and 0 otherwise
Amount of charged energy for vehicle 𝑣 at charger 𝑠 during epoch ℎ
Indicator: 1 if a vehicle is assigned to charger 𝑠, and 0 otherwise
Amount of charged energy for vehicle 𝑣 at charger 𝑠

6

𝑚𝑟𝑣

Indicator: 1 if request 𝑟 is assigned to vehicle 𝑣, and 0 otherwise

3.1. Problem description

Consider a ride-hailing system operated by a transport network company (operator) with a fleet of EVs.
Vehicles  are  equipped  with  dedicated  communication  devices  for  real-time  communication  to  the
operator’s control center of vehicle states (e.g. location, vehicle’s activity, e.g. idle, charging or serving
customers, SoCs of vehicles, etc.). Vehicles’ dispatching and charging operations are controlled by the
operator. Customers arrive randomly and send their ride requests via  a smartphone app by indicating
their  pickup  location  and  desired  pickup  time.  The  operator  applies  a  batch  assignment  method  for
vehicle dispatching per batch assignment epoch (e.g. 1 minute). Customers have limited patience, which
is quantified by a maximum waiting time threshold (assume identical for each customer). Furthermore,
we  assume  customers  are  engaged  to  use  the  service  when  their  waiting  time  is  below  the  above
threshold. We divide a full day (24 hours) into two periods: service operating hours (6:00–23:59) and off-
duty hours (0:00–5:59). We assume that the fleet size is much larger than the number of operator-owned
chargers. During service hours, vehicles’ charging operations can only occur at operator-owned charging
stations, and there is no charger-type-specific fee incurred for their use, assuming no (negligible) marginal
costs for the use of different types of chargers owned by the same fleet operator. However, at the end of
service  hours,  vehicles  can  recharge  at  their  own  facilities  or  at  other  public  charging  stations  for
overnight charging. We therefore assume vehicles are fully charged at the beginning of the day. Time-of-
use  (ToU)  energy  prices  (i.e.  the  electricity  price  varies  by  time  of  day)  are  considered.  Energy  costs
depend  on  the  amount  of  charged  energy  and  applied  energy  prices.  When  chargers  are  occupied,
vehicles have to wait. No overlap is allowed for each charger, i.e. only one vehicle at a time. Charging
facilities are assumed heterogeneous, and the number of chargers is fixed. Vehicles need to maintain a
minimum  reserve  level.  The  objective of the  operator  is to maximize  the  total profit  for  the  planning
horizon (6:00-24:00) under stochastic customer demand.

We  propose  a  sequential  MILP  approach  that  decomposes  vehicle  dispatching  and  charging
operations into different planning horizons. First, a day-ahead charging schedule planning model devises
vehicle-specific charging schedules to guide vehicles’ charging times and target SoCs after recharging for
each  charging  decision  epoch  (e.g.  30  minutes)  for  the  day  (Model  P1,  described  later).  This  plan  is
adapted by a reactive model, which adjusts the pool of go-charge vehicles based on current system state
(current  occupancy  state  of  chargers,  vehicles’  states  (location,  SoCs,  activities,  etc.),  and  anticipated
energy needs to the end of the day. An online vehicle-charger assignment model (Model P3) is applied to
determine where to charge to minimize the total charging operational time per assignment epoch. For
vehicle dispatching, a batch dispatching model (Model P2) is proposed to maximize the profit of vehicle-
customer  matching,  given  the  customer’s  maximum  waiting  time  and  vehicles’  SoC  constraints.  The
decision time intervals for both vehicle dispatching and the reactive model are based on a short-time
horizon (e.g., 1 minute).

The timeline of day-ahead charging schedule, online vehicle dispatch, and vehicle-charger assignment
models are described in Figure 1. Our approach includes a day-ahead charging plan (the upper part of
Figure  1)  and  an  online  optimization  and  simulation  during  the  day  (the  lower  part  of  Figure  1).  We
provide a high-level view of the interactions between different decision/system variables in these three
models.  Model  P1  optimizes  the  day-ahead  charging  schedule  plan  to  minimize  the  overall  charging
operation costs. The output of P1 provides a charging plan that indicates a sequence of sets of vehicles
that  need  to  recharge  (𝑉̃ℎ )  and  their  targeted  SoCs  after  recharging  (𝐸̅𝑣, ∀𝑣 ∈ 𝑉̃ℎ )  for  each  charging
decision epoch ℎ until the end of the day. During the day (online optimization), 𝑉̃ℎ are added to the pool
of  need-to-charge  vehicles 𝛀𝒕 at  time 𝑡 = ℎ∆ℓ for  h=1,2,3,…,  i.e., Ω𝑡 = Ω𝑡−1 ∪ 𝑉̃ℎ.  Then  the  relevant
subset 𝛀̃𝒕 (pool of to-charge vehicles at time t) from Ω𝑡 is filtered as the input for P3 based on Steps 9 to
13 in Algorithm 1. The solution for P3 is executed, and the SoCs of vehicles in Ω̃ 𝑡 are updated when the
vehicles arrive at the assigned chargers and when they complete their charging operations. The incurred
charging operation costs (𝐶̃𝑡) are collected at time t based on the output of P3. The pool of  need-to-
charge vehicles Ω𝑡 is then updated as Ω𝑡+1 at time t+1. Afterward, the idle vehicle set 𝑉𝑡 is updated to

7

serve unserved customer sets 𝑅𝑡 by solving P2. The execution of P2 at time t allows generating the net
𝑡 to be collected, and the system states (location of vehicles, cumulative waiting time of unserved
profit 𝑍2
customers, and SoCs of vehicles) are updated accordingly. For each day of service operation, the total
𝑡 − 𝐶̃𝑡 for 𝑡=1 to 𝑇 − 𝑇0. At the end of the day,  the operator collects  the
profit is the summation of 𝑍2
system  information  and  updates  the  input  parameters  (𝛿ℎ, 𝛾, 𝑊̅ℎ𝑠)  for P1  and  calculates  the  charging
schedule plan for the next day. The detailed description of Models P1 to P3 and the simulation framework
are presented in the following subsections.

Figure 1. Timeline of day-ahead charging schedule, vehicle dispatch, and vehicle-charger assignment. The
online vehicle-charger assignment (Model P3) and vehicle dispatch (Model P2) are solved and executed
at the beginning of each minute. Based on the executions, the system states (𝑆̃𝑡, 𝑉𝑡, Ω𝑡, 𝑒𝑣𝑡, 𝑅𝑡, 𝑊𝑅𝑡, and
vehicle  locations)  are  updated  accordingly,  i.e.,  either  unchanged  until  t+1  if  vehicles  remain  idle,  or
updated  at  the  end  of  the  event  (e.g.,  moving  to  chargers,  queueing  at  chargers,  charging,  serving
customers etc.). The above diagram only shows some system state variables where 𝑆̃𝑡: charger occupancy
states at time t; 𝑉𝑡: set of idle vehicles at time t, Ω𝑡: pool of need-to-charge vehicles at time 𝑡; 𝑒𝑣𝑡: SoC of
vehicle 𝑣 at time t; 𝑅𝑡: set of unserved customers at time t; 𝑊𝑅𝑡: set of cumulative waiting times up to t
for 𝑅𝑡.

3.2. Day-ahead charging schedule planning and online vehicle-charger assignment

To better utilize limited operator-owned chargers, a day-ahead charging schedule plan model is proposed
to minimize the overall charging operational costs by considering charging access costs, ToU energy costs,
and opportunity costs  for charging operations  (including charging time  and expected waiting time  for
charging). Let 𝑉 denote the set of vehicles, 𝑇 the planning horizon, and 𝑆 the set of chargers. 𝑇 is divided
into a set of charging decision epochs ℎ ∈ 𝐻̂ℓ = {1,2, … , ⌈
⌉} from 𝑇0 (the starting time of service, i.e.,
6:00  a.m.)  to  the  end  of  the  day  T  with  a  homogeneous  interval ∆ℓ, where ∆ℓ denotes  the  charging
schedule  planning  decision  time  interval.  The  day-ahead  charging  planning  model  aims  to  determine
when  and  target  SoC  for  each  epoch  in  𝐻̂ℓ  given  vehicles’  driving  (energy)  needs  and  charging
infrastructure constraints for the day. As charging speed decreases significantly when the vehicle’s SoC is
above  around  80%  of  its  battery  capacity  (Froger  et  al.,  2019),  vehicles  are  not  to  charge  above  this
threshold to save charging times during service hours. Based on historical driving data of vehicles, the
average consumption of vehicles for each charging decision epoch (i.e., 𝛿ℎ) can be calculated, and we can

𝑇−𝑇0
∆ℓ

8

identify the first epoch at the beginning of which the SoC of vehicles is below 80% (say ℎ’). The precedent
charging decision epochs of ℎ’ (ℎ < ℎ’, ∀ℎ ∈ 𝐻̂ℓ)  can be removed as the vehicles’ charging decision in
these epochs is irrelevant. Let 𝐻ℓ denote  the  set of the shifted  decision epochs for charging schedule
planning, i.e.,  𝐻ℓ = {1,2, … , 𝑛𝐻ℓ + 1} where 𝑛𝐻ℓ is the number of the charging decision epochs for the
planning horizon 𝑇. The first epoch ℎ in 𝐻ℓ corresponds to ℎ’ in 𝐻̂ℓ. The problem is formulated as a MILP
𝑣  vehicle 𝑣 is assigned to charger 𝑠 in epoch ℎ,
below in the space of 𝐻ℓ. The decision variables are: 𝑥ℎ𝑠
and 𝑦ℎ𝑠

𝑣  the amount of charged energy for vehicle 𝑣 at charger 𝑠 during epoch ℎ.

P1: Day-ahead charge schedule planning

min 𝑍1 = ∑ ∑ ∑ ((𝑝ℎ +
ℎ∈𝐻ℓ

𝑣∈𝑉

𝑠∈𝑆

𝛾
𝜑𝑠

)𝑦ℎ𝑠

𝑣 + (𝐶 + 𝛾𝑊̅ℎ𝑠)𝑥ℎ𝑠
𝑣 )

Subject to

≤ 1, ∀𝑣 ∈ 𝑉, ℎ ∈ 𝐻ℓ

≤ 1, ∀𝑠 ∈ 𝑆, ℎ ∈ 𝐻ℓ

𝑣
∑ 𝑥ℎ𝑠
𝑠∈𝑆
𝑣
∑ 𝑥ℎ𝑠
𝑣∈𝑉

𝑣
𝑒𝑣,ℎ+1 ≤ 𝑒𝑣ℎ − 𝛿ℎ (1 − ∑ 𝑥ℎ𝑠

𝑠∈𝑆

𝑣
𝑒𝑣,ℎ+1 ≥ 𝑒𝑣ℎ − 𝛿ℎ (1 − ∑ 𝑥ℎ𝑠

𝑣
) + ∑ 𝑦ℎ𝑠
𝑠∈𝑆

𝑣
) + ∑ 𝑦ℎ𝑠
𝑠∈𝑆

, ∀𝑣 ∈ 𝑉, ℎ ∈ 𝐻ℓ

, ∀𝑣 ∈ 𝑉, ℎ ∈ 𝐻ℓ

𝑠∈𝑆

𝛼𝑠 ≤ (

𝑣
𝑦ℎ𝑠
𝜑𝑠
𝑚𝑖𝑛 ≤ 𝑒𝑣ℎ ≤ 𝐸𝑣

𝐸𝑣

) + 𝑀1(1 − 𝑥ℎ𝑠

𝑣 ), ∀𝑣 ∈ 𝑉, ℎ ∈ 𝐻ℓ, 𝑠 ∈ 𝑆

𝑚𝑎𝑥, ∀𝑣 ∈ 𝑉, ℎ ∈ 𝐻ℓ ∪ {𝑛𝐻ℓ + 1}
𝑒𝑣1 = 𝐸𝑣

0, ∀𝑣 ∈ 𝑉

𝑣 ≤ 𝑀2𝑥ℎ𝑠
𝑦ℎ𝑠
𝑣 ≤ 𝑌𝑠
0 ≤ 𝑦ℎ𝑠
𝑣 ∈ {0,1}, ∀𝑣 ∈ 𝑉, ℎ ∈ 𝐻ℓ, 𝑠 ∈ 𝑆
𝑥ℎ𝑠

𝑣 , ∀𝑣 ∈ 𝑉, ℎ ∈ 𝐻ℓ, 𝑠 ∈ 𝑆
𝑚𝑎𝑥, ∀𝑣 ∈ 𝑉ℎ, ℎ ∈ 𝐻ℓ, 𝑠 ∈ 𝑆

(1)

(2)

(3)

(4)

(5)

(6)

(7)
(8)
(9)
(10)
(11)

The objective function (1) minimizes total charging costs for the planning horizon 𝐻ℓ. The first term in Eq.
𝑣  where 𝑝ℎ denotes the average energy price on ℎ. 𝜑𝑠 is the charging
(1) is related to charging costs for 𝑦ℎ𝑠
power of charger s. 𝛾 is the average profit per vehicle-minute traveled based on the realized customer
service/profit on the previous days. The second term is related to charging access distance costs 𝐶 and
expected waiting times 𝑊̅ℎ𝑠 when arriving at the charger 𝑠 at the beginning of epoch ℎ. Eqs. (2) and (3)
state that each vehicle can be assigned to at most one charger, and each charger can be assigned to at
most one vehicle for each ℎ, respectively. Eqs. (4) and (5) state vehicles’ SoC changes from ℎ to ℎ + 1
with the charged amount of energy when recharging and with average energy consumption 𝛿ℎ of vehicles
otherwise. Eq. (6) states that a minimum charging time 𝛼𝑠 (e.g. 10 minutes) is implied for each charging
operation. Eq. (7) and (8) set the range of 𝑒𝑣ℎ and the initial battery level 𝐸0 at the beginning of ℎ = 1,
𝑣 . Eq. (10) ensures the maximum amount of energy can be recharged
respectively. Eq. (9) binds 𝑥ℎ𝑠
from  charger 𝑠  during  one  charging  decision  epoch. 𝑀1  and 𝑀2  are  positive  numbers  with 𝑀1 = 𝛼𝑠
𝑚𝑎𝑥}
where 𝛼𝑠 is the minimum charging time per charging operation for charger 𝑠, and 𝑀2 = 𝑚𝑎𝑥𝑠∈𝑆 {𝑌𝑠
𝑚𝑎𝑥 is the maximum amount of energy that can be charged on charger 𝑠 during one charging
where 𝑌𝑠
decision  epoch.  The  model  parameters 𝛿ℎ, 𝑊̅ℎ𝑠, 𝛾, and 𝐶 can  be  estimated  based  on  historical  vehicle
driving and charging data.

𝑣  and 𝑦ℎ𝑠

Based on the outputs of P1 (i.e., the solution of 𝑒𝑣ℎ, 𝑥ℎ𝑠

𝑣 ), the operator obtains a schedule to
assign  vehicles  to  charge  and  their  target  SoCs  after recharge  over 𝐻̂ℓ.  This  schedule  is  then  adapted
based on a reactive model to determine the amount of energy to be charged and where to charge for
vehicles. This reactive model maintains a pool of go-charge-vehicles based on the charging plan (excluding
vehicles currently serving customers), which is adapted with additional vehicles to recharge; either with

𝑣  and 𝑦ℎ𝑠

9

low SoC (i.e. less than 20% of their battery level) or previously delayed vehicles for charging or due to the
number of go-charge-vehicles exceeds the number of chargers. An online vehicle-to-charger assignment
model below is applied to minimize total charging operational times for vehicle-to-charger assignment.
A more detailed description is presented in the simulation framework (Algorithm 1). The online vehicle-
to-charger assignment problem is formulated as a MILP as follows.

3.3. Vehicle dispatch and vehicle-charger assignment

We  adopt  a  batch  dispatch  optimization  approach  to  match  unserved  requests  with  idle  vehicles.
Customer arrivals are stochastic and grouped into batches at the beginning of each decision epoch. A
batch dispatching optimization is executed at the beginning of each batch decision epoch to maximize
the profit of serving customers. As the stochastic demand is revealed in real-time, the operator’s profit
maximization  problem  cannot  be  optimized  for  the  entire  day,  but  instead  must  be  optimized  in  a
sequential  way  based  on  customer  arrivals  every  minute.  Existing  studies  formulate  this  problem  by
neglecting the cumulative waiting time of customers in the unserved pool, resulting in customers leaving
due to high waiting times (Ahadi et al., 2023). Different from the previous study, we integrate customers’
maximum  waiting  time  into  the  vehicle  dispatching  model  to  maximize  the  total  profit  of  vehicles’
dispatches. Let 𝑅𝑡 denote the pool of unserved requests at the beginning of batch dispatch epoch 𝑡 with
the time interval ∆𝑡 = 1 (minute), and 𝑉𝑡 the set of idle vehicles at 𝑡. The batch dispatching problem at
the beginning of epoch 𝑡 (i.e., 𝑡 minutes from the start of the planning horizon) is formulated as a MILP
problem. The decision variable is 𝑚𝑟𝑣, determining the vehicle-to-request assignment. 𝑒𝑣𝑡 and 𝑊𝑟𝑡 are
the  SoC of  vehicle 𝑣 and  the  cumulative  waiting  time of customer 𝑟 at the  beginning  time  of  epoch 𝑡,
respectively. The problem is solved every minute, after which the system state is updated accordingly
(i.e., a vehicle’s SoC is updated after each ride or displacement (for charging), and 𝑊𝑟𝑡 is updated every
minute). The inter-epoch system state updating is executed in the simulation (see Algorithm 1).

P2: Batch dispatch

max 𝑍2

𝑡 = ∑ ∑ (𝛽0 + 𝛽1𝑑̅𝑜𝑟𝑑𝑟 − 𝜋(𝑑̅𝑜𝑟𝑑𝑟 + 𝑑̅𝑣𝑜𝑟))𝑚𝑟𝑣

Subject to

𝑟∈𝑅𝑡

𝑣∈𝑉𝑡

∑ 𝑚𝑟𝑣
𝑣∈𝑉𝑡
∑ 𝑚𝑟𝑣
𝑟∈𝑅𝑡

≤ 1, ∀𝑟 ∈ 𝑅𝑡

≤ 1, ∀𝑣 ∈ 𝑉𝑡

𝑚𝑖𝑛 ≤ 𝑒𝑣𝑡 − 𝜇(𝑑̅𝑜𝑟𝑑𝑟 + 𝑑̅𝑣𝑜𝑟) + 𝑀3(1 − 𝑚𝑟𝑣), ∀𝑟 ∈ 𝑟𝑡, 𝑣 ∈ 𝑉𝑡
𝐸𝑣
𝑊𝑟𝑡 + 𝑡̅𝑣𝑜𝑟𝑚𝑟𝑣 ≤ 𝑊𝑚𝑎𝑥, ∀𝑟 ∈ 𝑟𝑡, 𝑣 ∈ 𝑉𝑡
𝑚𝑟𝑣 ∈ {0,1}, ∀𝑟 ∈ 𝑅𝑡, 𝑣 ∈ 𝑉𝑡

(12)

(13)

(14)

(15)
(16)
(17)

The objective function (12) maximizes the profit of vehicle dispatch at time 𝑡 where the net profit of a
customer-vehicle  match  (𝑟, 𝑣)  is  calculated  as  the  difference  of  the  service  fare  𝛽0 + 𝛽1𝑑̅𝑜𝑟𝑑𝑟  and
vehicle’s  travel  cost 𝜋(𝑑̅𝑜𝑟𝑑𝑟 + 𝑑̅𝑣𝑜𝑟), where  𝑑̅𝑜𝑟𝑑𝑟  is  the  trip  distance  of  request 𝑟 ,  and  𝑑̅𝑣𝑜𝑟  is  the
distance from the vehicle’s current location to pick up customer 𝑟 at 𝑜𝑟. The service fare is composed of
a base rate 𝛽0 and a distance-based operating fee 𝛽1𝑑̅𝑜𝑟𝑑𝑟. Constraints (13)-(14) ensure that one vehicle
can serve at most one customer and vice versa. Constraint (15) ensures that a matched vehicle needs to
have sufficient energy to reach the pickup location of the assigned customer and serve that trip (i.e., the
vehicle’s  SoC  needs  to  be  no  less  than  a minimum  level  after  subtracting  the energy  consumption  of
serving that ride from its current SoC). Energy consumption is assumed proportional to the travel distance
with  a  constant  energy  consumption  rate 𝜇. Constraint  (16)  ensures  customers'  waiting  time  cannot
exceed  a  maximum  threshold 𝑊𝑚𝑎𝑥  (e.g.,  7-10  minutes).  Note  that 𝑊𝑟𝑡  is  customer 𝑟 ’s  cumulative
waiting time up to 𝑡. 𝑀3 is a positive number based on the bigM method to solve the mixed integer linear
10

programming  problem.  We  set 𝑀3 at  its  smallest  value  without  removing  any  legitimate  solutions  as
𝑚𝑎𝑥. Note that unassigned customers wait in the system to be assigned until the next decision epoch
𝐸𝑣
𝑡 + 1. If a customer’s maximum waiting time is reached, they leave the system and are not served by the
service. The SoCs of vehicles are updated as follows. For matched vehicles, their SoCs are updated at the
time  of  dropping  off  their  assigned  customers.  Let  ∆𝑡𝑟𝑣 = (𝑡̅𝑜𝑟𝑑𝑟 + 𝑡̅𝑣𝑜𝑟)  be  vehicle  𝑣 ’s  travel  time
(calculated  as  total  travel  distance  divided  by  the  average  speed  of  vehicles)  from  vehicle’s  current
location to pick up customers at 𝑜𝑟 and drop off customers at 𝑑𝑟. We update SoCs for matched vehicles
as  𝑒𝑣,𝑡+∆𝑡𝑟𝑣 = 𝑒𝑣𝑡 − 𝜇(𝑑̅𝑜𝑟𝑑𝑟 + 𝑑̅𝑣𝑜𝑟).  For  unmatched  vehicles  (remaining  idle),  their  SoCs  remain
unchanged until t+1, i.e., 𝑒𝑣,𝑡+1 = 𝑒𝑣𝑡.  For the waiting times of unserved customers, their waiting times
at 𝑡 + 1 are updated as 𝑊𝑟𝑡 + 1. If the waiting times of these unserved customers exceed 𝑊𝑚𝑎𝑥, these
customers leave the system. The net profit from serving customers to the end of the day is the summation
of 𝑍2

𝑡 from 𝑇0 to 𝑇.

P3: Online vehicle-charger assignment

We utilize two different sets to manage online vehicle-to-charger assignment. Let Ω𝑡 be the set of need-
to-charge vehicles at time t, and Ω̃𝑡 be the subset of Ω𝑡 that are relevant (i.e. needs to satisfy several
criteria, see Algorithm 1 and the explanation around it) to be assigned to chargers for recharging at time
t. Given the current decision epoch 𝑡 (same as the batch assignment, corresponding to 𝑡 minutes from
the beginning of the service), the current location of vehicles and the utilization state of chargers, the
objective function (18) aims to minimize the total charging access time (𝑡̅𝑣𝑠) and waiting time (𝑊̅𝑣𝑠), and
charging  time  (𝓎𝑣𝑠/𝜑𝑠)  of  the  assignment  of  vehicles  to  chargers.  The  decision  variables  are:  𝑥̂𝑣𝑠
whether  a  vehicle 𝑣 is  assigned  to  a  charger 𝑠,  and 𝑦̂𝑣𝑠  the  amount  of  energy  vehicle 𝑣 charges  at  a
charger. 𝑒𝑣𝑡 is the SoC of vehicle 𝑣 at the beginning time of epoch t. Given the current utilization state of
chargers, 𝑊̅𝑣𝑠  is  the  waiting  time  that  vehicle 𝑣 would  experience  if  it  departs  immediately  to  go  to
charger 𝑠. The operator looks across all current charger queues and obtains the waiting time for every
charger.  This  information  can  be  obtained online  from the  operator's  charging  network  management
system.

min 𝑍3 = ∑ ∑((𝑡̅𝑣𝑠+𝑊̅𝑣𝑠)𝑥̂𝑣𝑠
𝑠∈𝑆

𝑣∈Ω̃ 𝑡

+ 𝑦̂𝑣𝑠/𝜑𝑠)

𝑆𝑢𝑏𝑗𝑒𝑐𝑡 𝑡𝑜

= 1, ∀𝑣 ∈ Ω̃𝑡

≤ 1, ∀𝑠 ∈ 𝑆

∑ 𝑥̂𝑣𝑠
𝑠∈𝑆
∑ 𝑥̂𝑣𝑠
𝑣∈Ω̃ 𝑡

0 ≤ 𝑒𝑣𝑡 − 𝜇𝑑̅𝑣𝑠𝑥̂𝑣𝑠 + 𝑀4(1 − 𝑥̂𝑣𝑠), ∀𝑣 ∈ Ω̃𝑡, 𝑠 ∈ 𝑆
𝐸̅𝑣 ≤ 𝑒𝑣𝑡 − 𝜇𝑑̅𝑣𝑠𝑥̂𝑣𝑠 + 𝑦̂𝑣𝑠 + 𝑀4(1 − 𝑥̂𝑣𝑠), ∀𝑣 ∈ Ω̃𝑡, 𝑠 ∈ 𝑆

𝛼𝑠 ≤ (

) + 𝑀5(1 − 𝑥̂𝑣𝑠), ∀𝑣 ∈ Ω̃𝑡, 𝑠 ∈ 𝑆

𝑦̂𝑣𝑠
𝜑𝑠
𝑦̂𝑣𝑠 ≤ 𝑀6𝑥̂𝑣𝑠, ∀𝑣 ∈ Ω̃𝑡, 𝑠 ∈ 𝑆

0 ≤ 𝑦̂𝑣𝑠 ≤ 𝑌𝑠

𝑚𝑎𝑥, ∀𝑣 ∈ Ω̃𝑡, 𝑠 ∈ 𝑆

𝑥̂𝑣𝑠 ∈ {0,1}, ∀𝑣 ∈ Ω̃𝑡, 𝑠 ∈ 𝑆

(18)

(19)

(20)

(21)
(22)

(23)

(24)
(25)
(26)

Constraints (19) and (20) ensure that each vehicle is assigned to exactly one charger, and each charger
can be connected to at most one vehicle when the number of to-recharge vehicles is no less than that of
chargers. In the other case, these two equations are replaced by Eqs. (27)-(28).

≤ 1, ∀𝑣 ∈ Ω̃𝑡

∑ 𝑥̂𝑣𝑠
𝑠∈𝑆

11

(27)

= 1, ∀𝑠 ∈ 𝑆

∑ 𝑥̂𝑣𝑠
𝑣∈Ω̃ 𝑡

(28)

Eq. (21) ensures that the vehicle’s SoC is always non-negative when arriving at the charger’s location. Eq.
(22) states that vehicle 𝑣 needs to be recharged to the target SoC 𝐸̅𝑣 based on the day-ahead charging
plan. Note that if a vehicle is delayed in being added to the pool due to serving customers, its target SoC
remains the planned one based on the output of P1. As aforementioned, when the additional go-charge
vehicles’ SoCs are below the threshold 𝜃𝐵 (i.e. 20% of their battery capacity), they are added to the pool.
These vehicles’ respective target SoCs are set based on the average energy consumption 𝛿ℎ (estimated
from  historical  data)  by  anticipating  their  energy  consumption  to  the  end  of  the  day.  To  maximize
𝑚𝑖𝑛. For this
vehicles’ availability, vehicles’ SoC at the end of the day should be as close as possible to 𝐸𝑣
purpose,  we  apply  the  following  rule  to  determine  vehicles’  target  SoCs  when  their  SoCs  are  below
𝑡 denote vehicle 𝑣’s SoC at 𝑡, and ℎ(𝑡) be the corresponding ℎ index of 𝑡. The target SoC of
𝜃𝐵. Let 𝑆𝑜𝐶𝑣
vehicle 𝑣 when adding it to the to-charge vehicle pool at t is defined as

𝑆𝑜𝐶𝑣

𝑡𝑎𝑟𝑔𝑒𝑡(𝑡) =  𝑚𝑖𝑛 (𝐸̃𝑣, 𝑆𝑜𝐶𝑣(𝑡) + 𝐸⃗ 𝑣(𝑡))

(29)

𝑛
𝐻ℓ
where 𝐸⃗ 𝑣(𝑡) is the energy needed to the end of the day, calculated as 𝐸⃗ 𝑣(𝑡) = ∑
ℎ=ℎ(𝑡) − 𝑚𝛿ℎwith 𝑚
𝛿ℎ
𝑚𝑖𝑛(i.e. 𝑚𝛿ℎ ≤
being the approximated number of epochs whose total energy consumption is around 𝐸𝑣
𝑚𝑖𝑛, given vehicles’
𝑚𝑖𝑛). In doing so, Vehicles’ SoCs at the end of the day would be a little more above 𝐸𝑣
𝐸𝑣
current  SoC  is  around 𝜃𝐵 where 𝐵 denotes  the  vehicle’s  battery  capacity.  To  further  reduce  vehicles’
waiting time for charging, we can  set 𝐸̃𝑣 as 𝑟𝑎𝑛𝑑(0.5𝐵, 𝐸𝑣
𝑚𝑎𝑥) .  This policy is more flexible than using
𝑚𝑎𝑥 as vehicles can recharge again sometime later as far as their SoCs are below 𝜃𝐵. Eq. (23) ensures a
𝐸𝑣
minimum charging time 𝛼𝑠 when vehicles go charging. 𝜑𝑠 is the charging rate of charger 𝑠. Eq. (24) binds
the  variables 𝑥̂ and 𝑦̂.  Eq.  (25)  specifies  the  maximum  energy  that  can  be  charged  for  one  charging
𝑚𝑎𝑥, 𝛼𝑠 , and 𝑌𝑠
decision epoch. 𝑀4, 𝑀5 and 𝑀6 are set as 𝐸𝑣

𝑚𝑎𝑥, respectively.

The SoCs of vehicles are updated based on the execution of the solution from P3. The set of 𝑉𝑡 and
Ω𝑡 is  updated  by  removing Ω̃𝑡 (these  vehicles  are  assigned  to  chargers  for  recharge).  If  a  vehicle 𝑣 is
assigned to charger 𝑠, its SoC is updated when arriving at the charger as 𝑒𝑣,𝑡+𝑡̅𝑣𝑠 =   𝑒𝑣𝑡 − 𝜇𝑑̅
𝑣𝑠, where 𝜇
is the vehicle's discharging rate per kilometer traveled. When arriving at the assigned charger s, vehicle’s
SoC  is  updated  at  the  end  of  their  charging  operation,  including  queueing  times  (𝑊̅𝑣𝑠 )  and  charging
= 𝑒𝑣𝑡 − 𝜇𝑑̅𝑣𝑠 + 𝑦̂𝑣𝑠. In terms of charging operation costs, let 𝐶̃𝑡 be
duration  (

), i.e., 𝑒

𝑦̂𝑣𝑠
𝜑𝑠

𝑣,𝑡+𝑡̅𝑣𝑠+𝑊̅𝑣𝑠+

𝑦̂𝑣𝑠
𝜑𝑠

𝑠∈𝑆

𝑡
𝑍2

𝑡
𝑍2

𝑣∈Ω̃ 𝑡

− ∑

𝑇−𝑇0
𝑡=1

𝑇−𝑇0
𝑡=1

∑ (𝜋𝑑̅𝑣𝑠𝑥̂𝑣𝑠

the total access costs and charging costs incurred after executing the solution from P3 at time 𝑡, defined
as 𝐶̃𝑡 = ∑
+ 𝑝𝑣𝑠𝑦̂𝑣𝑠) where 𝜋 is the cost per kilometer traveled, and 𝑝𝑣𝑠 is the average
energy price when the vehicle starts to charge at time 𝑡 + 𝑡̅𝑣𝑠 + 𝑊̅𝑣𝑠. The daily total charging operation
cost, including access costs and energy costs, is defined as  𝐶̃ = ∑
. The total daily profit to the
end of the day is then defined as 𝑍 = ∑

𝑇−𝑇0
𝑡=1
Note that if no feasible solutions can be found for Ω̃𝑡, vehicles with the highest SoCs are removed
from Ω̃𝑡, and then the problem is solved again until the optimal solution is found. The removed vehicles
remain idle and can be dispatched to serve customers. If the removed vehicles are not dispatched for
serving customers (remain idle) during 𝑡, they are added to the pool Ω𝑡 for charging at 𝑡 + 1. Note that
for each vehicle-to-charger assignment epoch t, Ω𝑡 is filtered by retaining a subset of vehicles in Ω𝑡 where
the calculated amount of energy to be charged (depending on vehicles’ current SoC and their target 𝐸̅𝑣)
needs to be at least equivalent to the amount of charging 𝛼 minutes (minimum charging duration) on a
fast charger. If the amount of energy to be charged is below this minimum amount of energy, vehicles
remain idle for serving customers. In doing so, multiple short-duration recharging operations with short
charging times can be avoided, significantly reducing the operator's total charging access costs.

𝐶̃𝑡

.

Algorithm 1 presents the pseudocode of the simulation framework. The simulation technique is based
on the discrete event simulation technique but integrates vehicle dispatching and charging decisions for
each  short  planning  horizon  (1  minute).  Vehicle  state  can  be  one  of  the  following  ones:  idle,  serving

12

customers, go-charging (moving to charging station), queueing (for charging) and charging. Vehicle state
change can be triggered at the end of an event or by the online optimization models for vehicle dispatch
or  charging.  For  example,  an  idle  vehicle  changes  its  state  to  serving customers  based on  the  vehicle
dispatch model at time t. When dropping off customers or completing charging operations, vehicle state
changes to idle. Step 1 reads the input data. Step 2 estimates the parameters used for the day-ahead
charging planning model (described in more detail in Sect. 4). Step 3 solves P1 to obtain the day-ahead
charging plan of vehicles. Step 4 sets up the initial condition for the simulation. Step 5 is the loop of the
simulator  clock  for  batch  dispatching  where  𝑡  corresponds  to  minutes  after  the  start  (6:00),  and 𝑇
corresponds to the end of the day (24:00). Note that we use continuous time to track the system state in
the simulator. Steps 6 to 8 add vehicles to the pool based on the day-ahead charging plan. Step 9 adds
additional vehicles to the pool if their SoCs are below the threshold 𝜃𝐵. Steps 10-13 filter idle vehicles in
the pool and assign them to chargers for recharge by solving P3. Steps 14-16 update the list of idle vehicles
and unserved customers and dispatch vehicles to serve customers based on P2. Then update the system
state until the end of 𝑡. Note that time is continuous in our simulation implementation and the system
state is updated accordingly with the occurring times of different events.

Algorithm 1. Simulation framework for dynamic charging planning, vehicle-to-charger assignment, and
batch dispatch.

1.
2.

3.

4.

5.
6.
7.
8.
9.
10.

11.
12.

13.
14.

15.

16.
17.

  Input: Time-dependent energy prices, customer demand, a fleet of vehicles, and charging facilities.
  Compute the average energy consumption (𝛿ℎ) and average charging waiting times (𝑊̅ℎ𝑠) of vehicles
at chargers per charging decision epoch up to the previous day.
 Solve the day-ahead charging planning problem P1 to get initial charging plans of vehicles (𝑉̃ℎ, 𝐸̅
𝑉̃ℎ) for the planning horizon (i.e. 6:00-24:00).
 Initialization: Initialize SoCs and locations of vehicles. Initialize a sequence of sets of idle vehicles for
each minute t, i.e. 𝑉0 = 𝑉,  𝑉1 = 𝑉2 = ⋯ = 𝑉𝑇−𝑇0 = ∅. Set the pool of need-to-charge vehicles as
empty, i.e., Ω0 = Ω1 = ⋯ = Ω𝑇−𝑇0 = ∅.
 for 𝑡 = 1,2, … , 𝑇

𝑣, 𝑣 ∈

  If 𝑡 mod ∆ℎ = 0
  Add the planned need-to-charge vehicles 𝑉̃ℎ|ℎ=𝑡/∆ℎ to Ω𝑡
  End
  Find the subset of idle vehicles in 𝑉𝑡 with SoCs lower than 𝜃𝐵 and add them to Ω𝑡.
  Find the subset of vehicles Ω̃𝑡 in Ω𝑡 that are idle and must charge to their target SoCs satisfying a
minimum amount of charged energy requirement.
  If Ω̃𝑡  is not empty

Solve P3 for Ω̃𝑡 and assign vehicles to their assigned chargers, execute their charging operations,
and update vehicle state. When a vehicle completes its charging operation at time t’, it becomes
idle immediately and is added to the set of idle vehicle 𝑉⌈𝑡’⌉. If there are no solutions, relocate the
vehicle with the highest SoC from Ω̃𝑡 and solve P3. Continue until a feasible solution is found.

  End
  Update the lists of unserved customers 𝑅𝑡. Remove vehicles going for charging (Ω̃𝑡) from the list of
idle vehicles 𝑉𝑡 and Ω𝑡.
  Solve the batch dispatching problem P2, dispatch vehicles to serve customers, and update the state
of vehicles (SoCs and locations). Update 𝑉𝑡  by removing these vehicles at time t and update the
corresponding sets of idle vehicles when dropping off customers.
  Update the system state to the beginning of 𝑡 + 1.

 End

3.4. Benchmark charging policies

To validate the proposed methodology, four benchmark charging policies selected from the literature are
compared. These  policies assume  that  vehicles  go  to  recharge  when their  SoCs  are  lower than  a  pre-
defined threshold. Different from existing studies that assume vehicles are willing to wait without limits
at  a  charger  (Jamshidi  et  al.,  2021),  we  consider  more  realistic  queuing  scenarios  at  chargers  for  the
benchmark policies by assuming a maximum waiting time limit in a queue (i.e. 15 minutes, identical for

13

all vehicles). Vehicles are assigned to chargers based on the used charging policy. When arriving at the
assigned charging stations, if the waiting time exceeds the maximum threshold, vehicles move away to
another  charger  with  the  least  waiting  time  when  their  SoCs  are  feasible  to  reach  there.  In  case  the
vehicle’s SoC is too low to reach the targeted charger, vehicles go to the nearest one (if the vehicle’s SoC
is feasible) or remain at the same charger (if the vehicle’s SoC is not feasible). This allows not to have
unrealisticly  too  long  queue  at  charging  stations.  The  benchmark  charging  policies  are  described  as
follows.

a.  Nearest charging policy (Nearest)(Bischoff and Maciejewski, 2014):  Vehicles  go to the nearest
𝑚𝑎𝑥 (i.e. 80% of their battery capacity) when their SoCs are below the

charger to recharge to 𝐸𝑣
threshold 𝜃𝐵 (i.e. 20% of their battery capacity).

b.  Fastest charging policy (Fastest): Vehicles go to the fastest charger to recharge to 𝐸𝑣

𝑚𝑎𝑥 when
their SoCs are below the threshold 𝜃𝐵. In case there is more than one fastest charger, a randomly
selected one is used. Note that if charging demand on fast chargers is not high (no congestion),
one can assign vehicles to the nearest one. On the contrary, when the number of fast chargers is
scarce,  using  this  random-assignment  policy  allows  not  to  assign  too  many  vehicles  to  a
geographically  well-situated  charging  station  (e.g.  the  one  located  at  the  middle  of  our  study
area), resulting in over-saturated utilization of certain fast chargers/charging stations.

c.  Charging  operational  time  minimization  approach  (MinChgOpT)(Ma  and  Xie,  2021):  When
vehicles’  SoCs  are  below  the  threshold,  vehicles  are  assigned  to  the  charger  with  minimum
𝑚𝑎𝑥, including access time, waiting time when arriving
charging operational time to charge to 𝐸𝑣
at chargers and charging time.

d.  Dynamic charging threshold policy (DynaThreshold)(Ahadi et al., 2023): Different from the above
benchmark  policies,  DynaThreshold  activates  vehicles’  charging  operations  earlier  when  their
SoCs  are still much higher than the threshold in order  to avoid charging during peak  charging
demand periods in the afternoon. In doing so, vehicles can save (charging) waiting time and the
charging  facility  can  be  utilized  more  effectively.  We  adopt  the  hourly  dynamic  charging
thresholds  used  in  Ahadi  et  al.  (2023),  where  the  average  hourly  charging  threshold  in  the
morning is around 50% while it becomes around 30% in the afternoon (see Table 1). When going
𝑚𝑎𝑥  so  we  expect  that  vehicles  charges  fewer  amount  of
charging,  vehicles  are  charged  to 𝐸𝑣
energy compared to the situation in the afternoon.

Table 1. Dynamic hourly SoC threshold for activating charging operations (Ahadi et al., 2023).
Hour (morning)
4
1
SoC threshold (𝜃)*    0.45
Hour (afternoon)
13
SoC threshold (𝜃)
 *: % of vehicles’ battery capacity.

11  12
7
0.4  0.4
0.6  0.65  0.62  0.58  0.55  0.52
19
23  24
14
0.2  0.25  0.27  0.35  0.35  0.4

17
15
0.38  0.35  0.32  0.25  0.25

10
0.4
22

8
0.5
20

9
0.4
21

18
0.2

16

3

5

6

2

4. Computational study

In this section, we first describe the test instance and parameter setting based on Manhattan yellow taxi
data. Then we present the computational results for different demand scenarios. A sensitivity analysis is
conducted to evaluate the impact of different model parameters.

4.1. Test instance generation

We  test  the  proposed  dynamic  charging  planning  approach  on  a  Manhattan-like  4X20  km2  area.  We
assume that the fleet size is 100 homogeneous EVs. Demand data is randomly drawn from the trips of
New York yellow taxi data1 on a typical weekday  in July  2019. The  service  operating hours  are  6:00  –

1 https://www.nyc.gov/site/tlc/about/tlc-trip-record-data.page

14

24:00. Two demand scenarios are considered: low demand with 3000 customers/day and high demand
with 4000 customers/day. As a comparison, the average daily trips per yellow taxi in July 2019 was 20.5
trips, according to the Taxi and Ride-hailing Usage in New York City dashboard2. As the customer’s origins
and  destinations  are  unavailable  (only  the  taxi  zones  of  customer  pick-up  and  drop-off  locations  are
available), we generate them randomly in the study area with an assumed minimum trip length of 5 km
which might be somewhat higher than real trip distance in Manhattan. We assume that the origins of
customers’ requests are within the 4X20 km2 area, while their destinations could be outside this area. We
randomly generate 15 independent customer demand datasets for each scenario, of which 10 are used
for  the  parameter  estimation  of  P1  (i.e.  𝛿ℎ ,  𝑊̅ℎ𝑠  and  𝛾 )  and  5  are  used  to  validate  the  proposed
methodology). For the operator-owned charging infrastructure, we assume there are 6 fast and 6 slow
chargers located at 4 different charging stations (i.e. each fast (slow) charging station has three fast (slow)
chargers, see Figure 1). We locate one fast charging station around the bottom center and another around
the center right based on the current public charging station locations in Manhattan3. The charging power
is assumed 50 kWh (fast) and 11kWh (slow), respectively. For the fleet, we assume that vehicles are fully
recharged  during  the  night  (the  overnight  charging  cost  is  not  the  operator's  concern)  at  their  initial
locations (assume they are randomly located in the study area). Acknowledging that overnight charging
costs might impact operators’ total profit, we provide more results in the sensitivity analysis, including
overnight charging costs for a fair comparison of different charging policies. Note that we can also add
additional constraints and flexibility (i.e., more available charging stations when charging overnight) to
incorporate overnight charging operations and ensure that the fleet is fully recharged at the beginning of
service  on  the  next  day.  Further  investigations  into  overnight  charging  scenarios  are  left  for  future
extension of this study.
Figure 1 illustrates the charging station locations and initial locations of vehicles in the study area. The
number of customer arrivals per 10 minutes for low and high-demand scenarios is shown in Figure 3. We
can observe that both demand profiles are very irregular with higher peaks during certain time slots (e.g.
8:00-10:00,  12:00-13:00,  and  15:00-18:00).  The  peak  demand  is  around  60  customer  arrivals  per  10
minutes. We assume that Nissan Leaf e+ is the used vehicle with a battery capacity of 62 kWh and an
energy consumption rate of 0.25 kWh/kilometer traveled (see Table 2). The impact of battery capacity
on the performance of the proposed methodology will be analyzed in the sensitivity analysis. For energy
prices, we assume that ToU energy prices change every 15 minutes based on the time-varying day-ahead
electricity prices, adapted to the real charging fee of NYC public charging stations. For simplification, we
assume that charging costs do not depend on the used type of chargers. In practice, there might have
supplementary fee for using fast chargers. For this purpose, we conduct a sensitivity analysis with energy
prices depending on charger  types.  Figure 4  shows the  ToU electricity prices  per  kWh charged over 4
consecutive days. The highest and lowest electricity prices are around 0.58 USD/kWh and 0.09 USD/kWh.
Note that other practical ToU energy prices can be applied in practice. The detailed parameter setting for
the computational study is shown in Table 2.

Table 2. Simulation parameter settings of the case study.
System parameter
Fleet size
Number of charging stations
Number of chargers1
Number of customers per day
Vehicle speed
Taxi fare2
Maximum waiting time of customers
Minimum charging duration (𝛼𝑠)
Battery capacity3 (𝐵𝑣)

Value
100
4
6 DC fast (50kW) and 6 slow chargers (11 kW)
3000 and 4000
30 km/hour
𝛽0 = $8 (base rate), 𝛽1 = 3.1 ($/km operating fee)
10 minutes
10 minutes
62 (kWh)

2 https://toddwschneider.com/dashboards/nyc-taxi-ridehailing-uber-lyft-data/
3 https://www.nyc.gov/html/dot/html/motorist/electric-vehicles.shtml#/find/nearest?location=NYC

15

Travel distance cost4 (𝜋)
0.53 (dollars/km)
Energy consumption rate3 (𝜑)
0.25 (kWh/km)
80% (10%) of 𝐵𝑣
𝐸𝑚𝑎𝑥(𝐸𝑚𝑖𝑛)
𝐸𝑖𝑛𝑖𝑡
62 (kWh)
Time-dependent energy price5
Day-ahead electricity Prices (15-minute resolution)
6:00-24:00
Service time
6:00-24:00
Charging planning horizon
Charge decision time interval (∆ℎ)
30 minutes
Batch dispatching time interval (∆𝑡)
1 minute
Remark: 1. Based on the two main charger types used in New York City (Taxi & Limousine Commission, 2022). 2. Approximated
base
based
surcharges
yellow
(https://www.nyc.gov/site/tlc/passengers/taxi-fare.page).  3.  Adapted
the  characteristics  of  Nissan  Leaf  e+
(https://evadept.com/calc/tesla-supercharger-charging-cost-calculator).  4.  Based  on  Ahadi  et  al.  (2023).  5.  Adapted  from
https://transparency.entsoe.eu/, biding zones GE_LU, July 2019.  The adapted electricity price variation range  covers the real
charge  fee  in  New  York  City  ($0.39  per  kWh  consumed;  see  https://www.nyc.gov/html/dot/html/motorist/electric-
vehicles.shtml#/dc).

includes

current

from

NYC.

fare

The

taxi

the

the

fee

on

in

Figure 2. Charging station distribution in the study area. There are 4 charging stations, each with three
chargers of the same type. A total of 6 DC fast chargers (50kW) and 6 slow chargers (11kW).

Figure 3. An example of customer arrival intensity per 10 minutes for two different demand scenarios.

16

Figure 4. Electricity prices per kWh charged for 24 hours.

4.2. Results

We test the performance of the CongestionAware charging policy on the test instances and compare it
with the benchmark approaches. The implementation is based on Julia on a laptop with Intel(R) Core(TM)
i7-11800H and 64 GB memory. The MILP models P1 to P3 are solved using Gurobi. We define a set of key
performance indicators (KPIs) to evaluate the performance of different charging policies, including total
profit (PF), revenue (TR), travel costs (TTC), charging costs (CC), energy charged (ENG), customer service
rate  (SR),  vehicle  kilometer  traveled  (KMT),  charging  waiting  time  (TW),  and  charging  time  (TC).  The
acronyms and used measurement units are shown in Table 3.

Table 3. Acronyms used in the tables of computational studies.

 Acronym  Meaning
PF
TR
TTC
CC
ENG
SR
KMT
TW
TC

Profit
Revenue
Travel costs
Charging costs
Amount of charged energy
Service rate
Vehicle-kilometer traveled
Charging waiting time
Charging time

Unit
1000 USD
1000 USD
1000 USD
1000 USD
kWh
 %
1000 kilometers
hour
hour

a. Model parameter estimation and base results

The model parameters for the day-ahead charging planning P1 are 𝐶, 𝛿ℎ, 𝛾, and 𝑊̅ℎ𝑠, which need to
be estimated based on historical driving and charging operations data. We estimate the average charging
access  cost 𝐶 as  approximately  $2.7  based  on  an  approximate  average  distance  cost  to  the  charging
stations. 𝛿ℎ is estimated by conducting a simulation using internal combustion engine vehicles. For 𝑊̅ℎ𝑠
and 𝛾, we simulate the system for the two demand scenarios using the Fastest charging policy and obtain
their  respective  averaged  values.  As mentioned  previously,  10  independent  datasets  are  used  for  the
simulation to obtain these parameters for each demand scenario. Then we test the performance of the
proposed method on the 5 test instances (days) and report the average results.

The results for two demand scenarios with 3000 and 4000 customers a day are shown in Table 4.
Compared with the benchmark, the CongestionAware policy has the highest profit for both scenarios.
Total profit increases 7.65%-10.69% for the c3000 scenario and 8.76%-15.05% for the c4000 scenario.
17

Regarding service rate, the CongestionAware policy outperforms the benchmark by increasing 7%-10.8%
and 7.9%-12.3% for the c3000 and c4000 scenarios, respectively. For the c3000 scenario, the benchmark
charging  policies  result  in  much  higher  total  charging  waiting  times  (doubled  or  tripled)  than  the
CongestionAware policy. The total charged time is almost doubled, and the total charged energy is higher
than the CongestionAware policy. As a result, the service rates of the benchmark policies are much lower
(from  -7.37%  to  -11.12%)  compared  with  the  CongestionAware  policy.  For  the  c4000  high-demand
scenario, similar results can be observed. The CongestionAware policy has much lower charging waiting
time and charging time than the benchmark policies, resulting in a higher service rate (76.5%) and profit
($88.08k). As the service rate is higher for the CongestionAware policy, which means (inevitably) more
KMT  to  serve  more  customers  with  more  energy  use  and  higher  TTC.  The  energy  used  per  served
customer  is  2.64  (2.77)  kWh  for  the  c3000  (c4000) scenario  for  the  CongestionAware  policy, which  is
lower (around -3.2% for the two scenarios) than the benchmark policies (2.71-2.73 kWh (c3000 scenario)
and 2.85-2.86 kWh (c4000 scenario). Note that among the benchmark policies, the DynaThreshold has
the best performance because vehicles go to recharge earlier and avoid charging congestions in the peak
charging demand period (to be explained below). The randomly generated customer demands give rise
to variability in the performance of each charging policy. Standard deviations of the KPIs are shown in
Table  5,  calculated  over the  5 validation datasets.  The  CongestionAware policy shows lower  standard
deviations across all KPIs, demonstrating that it is more stable in the face of demand variability. This is
particularly notable for those KPIs where CongestionAware has higher absolute values: profit, revenue
and  service  rate.  Additionally,  the  optimal  charging  focus  of  CongestionAware  is  highlighted  by  the
extremely low variability (by comparison) in total charged energy, charger waiting time.

Table 4. Comparison of the KPIs for different charging policies.
CC
Scenario

TTC

c3000
(3000
requests)

c4000
(4000
requests)

SR

KMT

Charging policy
Nearest
Fastest
MinChgOpT
DynaThreshold

PF
73.02
73.46
74.45
75.08
  CongestionAware  80.59
76.55
77.31
77.56
80.98

TC
TW
ENG
TR
94.1
88.93  14.72  0.89  2824  84.9%  27.8  111.7
94.1
94.0
89.52  14.83  0.92  2935  85.7%  28.0
92.6
77.1
90.67  15.02  0.94  3011  86.9%  28.3
97.2  107.8
92.06  15.31  1.06  3430  88.7%  28.9
52.4
97.93  16.07  0.80  2556  95.7%  30.3
36.0
93.1
93.12  15.54  0.82  2657  64.2%  29.3  136.1
93.0
94.07  15.69  0.84  2745  64.8%  29.6  100.4
94.37  15.75  0.85  2796  65.1%  29.7
93.0
99.2
99.41  16.62  1.15  3751  68.6%  31.4  135.7  120.3
68.5

Nearest
Fastest
MinChgOpT
DynaThreshold
CongestionAware  88.08  107.64  17.95  1.04  3280  76.5%  33.9

48.4

c3000
(3000
requests)

Charging policy
Nearest
Fastest
MinChgOpT
DynaThreshold

Table 5. Standard deviations of the KPIs for different charging policies.
ENG
Scenario
148
125
239
100
82
208
320
178
207
53

PF
0.50
0.66
0.52
0.57
  CongestionAware  0.39
0.89
Nearest
1.38
Fastest
1.07
MinChgOpT
DynaThreshold
0.64
CongestionAware  0.52

TTC
CC
0.13  0.04
0.14  0.04
0.14  0.07
0.14  0.03
0.10  0.03
0.18  0.07
0.31  0.11
0.19  0.06
0.15  0.07
0.07  0.02

TR
0.64
0.84
0.76
0.68
0.52
1.14
1.82
1.28
0.84
0.58

c4000
(4000
requests)

SR
0.79%
0.95%
0.96%
0.85%
0.53%
0.85%
1.43%
0.99%
0.74%
0.48%

KMT
0.2
0.3
0.3
0.3
0.2
0.3
0.6
0.4
0.3
0.1

TW
27.3
27.5
18.1
15.1
1.0
13.8
23.7
32.0
10.0
3.1

TC
3.9
2.6
6.5
4.6
1.6
4.5
6.9
3.9
4.9
2.7

Figures 5 and 6 analyze the number of vehicles charging (subfigures (b)) and of waiting (subfigures (c)) for
the day using different charging policies. Subfigure (a) shows the average waiting time at fast chargers
that vehicles would have experienced using the Fastest charging policy. For the c3000 scenario, Subfigure
18

(a) in Figure 5 shows the charging waiting times at fast chargers increase significantly from the 10th hour
from the beginning of service (16:00) to the 14th hour (20:00) when using the Fast charging policy. As a
result, the day-ahead charging plan model devises a charging plan to avoid vehicle charging and waiting
during peak charging demand hours. Subfigure (b) shows the CongestionAware charging policy activates
vehicle charging operations earlier to reduce charging congestion compared to the benchmark. During
peak charging demand hours (from 10th to 16th hours), the number of vehicles charging is around 14 per
30  minutes,  lower  than  the  benchmark  with  around  1  or  2  more  vehicles.  As  this  policy  anticipates
vehicles’ energy (driving) need to the end of the day, less energy is charged in the late evening, resulting
in a higher service rate and fewer vehicles charging and waiting. Subfigure (c) shows that using the first
three benchmark policies results in high charging congestion (more vehicles waiting for charging) during
the evening peak (from the 10th hour to the 14th hour) due to the increasing number of vehicles’ SoCs
falling below the threshold of 20% battery capacity. The charging demand decreases after the 14th hour
and then increases again in the late evening. For the DynaThreshold policy, the number of vehicles waiting
increases  gradually  from  the  6th  hour  until  the  end  of  the  day.  This  is  because  the  hourly  charging
thresholds for the second half of the day are lower (around 50% in the morning and 30% in the afternoon
on average), resulting in more vehicles charging and waiting at the chargers due to charging longer time
in  the  afternoon  and  evening,  and  insufficient  number  of  fast  chargers  in  the  system.  However,  this
DynaThreshold policy performs better than the other three benchmark policies as it applies a smarter
partial  recharge  policy.  For  the  c4000  scenario,  the  charging  congestion  starts  earlier  (mainly  located
between the 8th and 12th hours instead of between the 10th and 14th hours; see subfigures (a) of Figures
6 and 5) due to higher customer arrival intensity for the c4000 scenario. Consequently, the obtained day-
ahead  charging  plan  reacts  in  response  to  the  charging  waiting  time  signals,  resulting  in  significantly
higher charging operations in the early hours of the day. As the CongestionAware policy applies a smarter
partial recharge strategy (Eq. (29)) to delay vehicles’ charging operations when charging waiting time on
a queuing charger exceeds a maximum threshold (e.g. 30 minutes) and minimize the charging operational
times for online vehicle-to-charger assignment, it allows significantly increasing vehicles’ availability to
serve customers. Interestingly, the distribution of vehicles’ SoCs at the end of the day has similar medians
for  all  the  charging  policies  (around  7.3  kWh),  but  the  benchmark  policies  have  a  much  higher  75-
percentile (around 20kWh or more) compared with the CongestionAware policy (7.4kWh).

Figure 5. Comparison of number of vehicles charging, vehicles waiting, and SoCs of vehicles at the end
of the day (c3000 scenario).

Figure 6. Comparison of number of vehicles charging, vehicles waiting, and SoCs of vehicles at the end
of the day (c4000 scenario).

19

The histograms of the SoC of vehicles at the end of the day for c3000 and c4000 are shown in Figures 7
and 8. For the CongestionAware policy, the SoC of vehicles at the end of the day is strongly concentrated
𝑚𝑖𝑛 (6.2 kWh) and 10 kWh for both cases (80% or more of the fleet). For the other benchmark
between 𝐸𝑣
policies,  the  distributions  of  the  SoC  of  vehicles  at  the  end  of  the  day  for  both  cases  show  higher
𝑚𝑖𝑛 and 10 kWh. For c3000, the
concentration (40% for c3000 and 60% for c4000) within the range of 𝐸𝑣
distribution of SoC of vehicles at the end of the day is higher than that of c4000 due to lower KMT travelled
(lower customer demand). The average SoC per vehicle at the end of the day (aSoC) for different charging
policies is reported in Table 12. For the  CongestionAware policy, its aSoC is 9.6  kWh  and 7.4 kWh for
c3000 and c4000, respectively. For the benchmark approaches, the aSoC ranges from 19.4 kWh to 21.2
kWh  for  the  c3000  scenario  and  from  14.3  kWh  to  18.0  kWh  for  the  c4000  scenario,  respectively..
Assuming that charging costs is $0.16/kWh for overnight charging in NYC (more details can be found in
Section 4.3.d), we can calculate the worst extra cost of overnight charging for the fleet (100 vehicles) to
be  100*(21.2-9.6)*0.16  =  $0.185k  and  100*(18-7.4)*0.16  =  $0.169k  for  c3000  and  c4000  scenarios,
respectively. Given that the net profit of the CongestionAware policy is significantly higher compared to
the other benchmarks (at least $5.51k and $7.1k more for the c3000 and c4000 scenarios, respectively),
the impact of the overnight charging costs on the total profit is marginal.

Figure 7. Histograms of the SoCs of vehicles at the end of the day for different charging policies (c3000
scenario).

20

Figure 8. Histograms of the SoCs of vehicles at the end of the day for different charging policies (c4000
scenario).

b. Analysis of realized charging sessions and occupancy state of chargers

Figure 9 compares the distributions of charging session durations using different charging policies where
Subfigure (a) is related to the c3000 scenario while Subfigure(b) to c4000 scenario. The CongestionAware
policy has a significantly lower charging duration per charging session compared with the benchmark. For
the  c3000  scenario,  the  median  charging  session  duration  and  amount  of  charged  energy  for  the
CongestionAware policy is 19.3 minutes (S.D. = 9.2 minutes) and 15.4 kWh (6.6 kWh), respectively. For
the  c4000  scenario,  the  median  duration  of  charging  sessions  and  charged  amount  of  energy  is  23.7
minutes  (S.D.  =  13.5  minutes)  and  18.2  kWh  (S.D.  =  9.3  kWh),  respectively.  Compared  with  the
CongestionAware  policy,  the  median  charging  durations  of  the  benchmark  policies  are  much  higher
(around 50 minutes for both scenarios).

Figure 10 shows the number of vehicles on fast and slow chargers over different charging policies
where Subfigures (a) (fast chargers) and (b)(slow chargers) are related to using the benchmark policies,
while Subfigures (c) (fast chargers) and (d) (slow chargers) to using the CongestionAware policy. For the
CongestionAware policy, all fast chargers (6 in total) are almost fully occupied from the 10th to 16th hours.
The CongestionAware policy has a higher occupancy rate on fast chargers compared to the benchmark
between  the  5th  to  10th  hours.  For  slow  chargers,  using  the  benchmark  policies  results  in  a  higher
utilization rate of slow  chargers  (11kW)  in the  evening. This is because  vehicles move  away from fast
chargers after waiting for a maximum waiting time (15 minutes) and go to another fast/slow charger with
the least waiting times. Note that we might apply different waiting policies at chargers. We test the effect
of  applying  different waiting  policies  (i.e.  no  limit waiting,  charger-chasing  using  fast  chargers only  or
charger-chasing using fast or slow chargers). The results show the above charger-chasing policy has better
performance compared to the other two waiting policies (see Appendix A). The utilization rate on slow
chargers  is  very  low  (0  most  of  the  time  or  <1  between  the  10th  and  16th  hours)  when  using  the
CongestionAware policy. This is because the online vehicle-to-charge assignment model P3 minimizes the
total charging operation times (including charging access time, waiting time, and charging time) under
the constraints that the SoCs of vehicles after recharge need to be no less than their target energy levels
(Eq. (22)) and satisfy a minimum charged amount energy requirement. Given the fact that the charging
power of slow chargers is 11kWh, the maximum amount of energy can be charged  on a slow charger
during  one  charging  decision  epoch  (30 minutes)  is quite  limited  (5.5kWh).  If the  difference  between
vehicles’ target energy levels and their SoCs is higher than this amount, vehicles will not be assigned to

21

slow chargers. Consequently, slow chargers' utilization rate is much lower than that of fast chargers, for
which vehicles can get charged 25kWh for a 30-minute charging time.

Figure 9. Distribution of the charging session durations for the c3000 scenario (on the left) and the
c4000 scenario (on the right).

Figure 10. Comparison of the average number of vehicles on fast chargers (on the left) and slow chargers
(on the right) using different charging policies for the c3000 scenario.

c. Effects of vehicles’ energy need anticipation and time-of-use energy prices

For  the  CongestionAware  policy,  we  further  investigate  the  benefits  of  the  energy-need  anticipation
strategy to determine the target energy level (Eq. (29)) by comparing an alternative without using it, i.e.
𝑚𝑎𝑥 (80%) from their current battery levels. The results are shown in Table 6. We can
vehicles charge to 𝐸𝑣
observe that using this strategy allows for reducing vehicles’ charging waiting time (-14.7% to -18.4%) and
increasing customers’ service rate (+1.5 to +3.9%) and profits (+1.6% to +4.8%). When not applying this
anticipative strategy, the CongestionAware policy still significantly outperforms the benchmark in terms
of total profit and service rate (see Table 4). In terms of the benefits of applying ToU energy prices, Table

22

7 compares the KPIs with and without using ToU energy prices (i.e. using a constant energy price of 0.33
USD/kWh to get the day-ahead charging plan but applying ToU policy for the test instances). The results
show a small amount of cost savings could be obtained (CC column for the c3000 scenario) as the day-
ahead charging planning model P1 minimizes the total charging costs over the planning horizon. However,
its effect is less significant than using energy-need anticipation for the reactive model.

Table 6. Comparison of the CongestionAware policy with and without anticipating energy needs.
Scenario  Anticipate

ENG

TTC

CC

c3000  Yes
  No
c4000  Yes
No

TR
KMT
PF
97.93  16.07  0.80  2556  95.7%  30.3
80.59
79.34
96.72  15.98  0.99  3210  94.2%  30.1
88.08  107.64  17.95  1.04  3280  76.5%  33.9
84.04  102.80  17.13  1.14  3700  72.6%  32.3

SR

TW
36.0
30.7
48.4
39.5

TC
52.4
66.2
68.5
77.3

Table 7. Comparison of the CongestionAware policy with and without ToU energy prices.
Scenario  ToU
TTC
c3000  Yes
  No
c4000  Yes
No

TR
KMT
PF
97.93  16.07  0.80  2556  95.7%  30.3
80.59
80.46
97.83  16.08  0.82  2586  95.5%  30.3
88.08  107.64  17.95  1.04  3280  76.5%  33.9
88.00  107.55  17.96  1.03  3250  76.2%  33.9

TW
36.0
33.2
48.4
48.8

ENG

CC

SR

TC
52.4
53.4
68.5
68.0

4.3. Sensitivity analysis

In  this  section,  we  investigate  the  impact  of  different  model  parameters  on  the  performance  of  the
CongestionAware policy. These parameters include the maximum charging waiting times at a queuing
charger, battery capacity, number of fast and slow chargers in the system, and unbalanced fast and slow
charger numbers and demand variation. We analyze the impact of incorporating overnight charging costs
and the use of charger-type-specific tariffs on the system performance using different charging policies.

a. Impact of maximum charging waiting time of vehicles at a queuing charger

The maximum charging waiting time at a queuing charger affects vehicles’ availability to serve customers
as  the  operator  can  delay  vehicles’  charging  operations  (idle  for  serving  customers)  when  estimated
queuing time on the assigned charger (has minimum total charging operational time among all chargers)
exceeds the maximum threshold. Table 8 compares the performance using 20, 30, 40 minutes and no
maximum  waiting  time  limit  for  different  demand  scenarios.  We  can  observe  that  when  there  is  no
maximum charging waiting time, the profit is the lowest compared with the other cases, in particular for
high-demand scenarios (total charging waiting time is 227.4 hours for no-limit waiting compared with the
other cases (less than 70 hours)). This is because the number of fast chargers is very insufficient in the
system, and vehicles need to wait a long time at fast chargers if there are  no maximum charging time
limits. On the other hand, when limiting vehicles’ maximum waiting time at a queuing charger, vehicles
can be idle to serve customers. Note that when increasing this maximum threshold, the total waiting time
increases  accordingly.  However,  the  total  customer  service  rate  and  profit  increase  if  the  maximum
waiting time threshold is limited, as is the case for a threshold of no more than 40 minutes. In practice,
the operator could learn/adjust this threshold based on its day-to-day realized vehicle queuing patterns
and charging demands.

Table 8. Impact of maximum waiting time at chargers for the CongestionAware policy.

Max.
waiting
time*
20

Scenario
c3000

PF
80.49

TR
97.81

TTC
16.05

CC

ENG
0.79  2527

SR  KMT
95.6%  30.3

TW
28.7

TC
50.7

23

30
40
no limit
20
30
40
no limit

80.59
80.82
80.07
87.87
88.08
88.47
86.07

97.93
98.28
97.48
107.28
107.64
108.21
105.86

16.07
16.17
16.08
17.84
17.95
18.08
17.73

0.80  2556
0.81  2586
0.84  2657
1.02  3203
1.04  3280
1.06  3368
1.30  4177

95.7%  30.3
96.0%  30.5
94.9%  30.3
76.1%  33.7
76.5%  33.9
76.7%  34.1
74.7%  33.5

36.0
42.8
57.1
38.6
48.4
69.4
227.4

52.4
55.1
61.3
65.1
68.5
73.8
122.1

c4000

*: in minutes.

b. Impact of battery capacity

To  test  the  impact  of  battery  capacity,  we  consider  three  battery  sizes,  i.e.  62,  72,  and  82  kWh.  We
consider only the high demand scenario of 4000 customers with identical parameter settings (results for
c3000 scenario would draw similar conclusions). Table 9 compares the performance of different charging
policies. As expected, increasing the battery size could significantly increase the customer service rate
and  the  system's  profit  (i.e.,  the  customer  service  rate  increases  around  10%  for  different  charging
policies if the battery size is increased from 62kWh to 82 kWh). Compared with the benchmark policies,
the CongestionAware policy has higher profits and service rates for all battery sizes. When comparing
with the second-best benchmark policy (DynaThreshold), the profit and customer service rate increases
from 8.77% to 17.03% and from 7.9% to 15.1%, respectively. The results demonstrate that by increasing
the  battery  size  (given  the  same  charging  station  capacity  limit),  the  CongestionAware  policy  further
outperforms the benchmark. This is because when battery size (capacity) increases, vehicles’ charging
times  and  waiting  times  become  longer,  which  could  increasingly  harm  vehicles’  availability  when
charging to 80% for each charging operation. However, the CongestionAware policy devises a smarter
charging plan that anticipates vehicles’ charging waiting times and energy needs and adapts it (reactive
model)  to  minimize  total  system  costs,  resulting  in  more  effective  utilization  of  congested  charging
facilities.

CC

TTC

SR  KMT

62
kWh

Table 9. Impact of battery capacity on the KPI using different charging policies (c4000 scenario).
TC
TW
TR
Battery
ENG
PF
93.1
93.12  15.54  0.82  2657  64.2%  29.3  136.1
76.55
93.0
94.07  15.69  0.84  2745  64.8%  29.6  100.4
77.31
94.37  15.75  0.85  2796  65.1%  29.7
93.0
99.2
77.56
99.41  16.62  1.15  3751  68.6%  31.4  135.7  120.3
80.98
68.5
48.4
88.08  107.64  17.95  1.04  3280  76.5%  33.9
89.0
98.33  16.42  0.83  2595  68.5%  31.0  127.8
80.89
89.1
98.66  16.48  0.86  2725  68.8%  31.1  122.8
81.09
81.87
91.7
99.63  16.65  0.90  2866  69.6%  31.4  120.3
85.07  104.01  17.39  1.07  3469  72.6%  32.8  116.3  111.7
59.5
94.30  114.94  19.22  0.94  2954  82.3%  36.3
40.3
77.9
84.66  102.77  17.16  0.75  2315  72.4%  32.4  121.8
78.5
84.95  103.19  17.24  0.79  2450  72.6%  32.5  119.7
79.7
85.40  103.74  17.33  0.81  2508  73.1%  32.7  117.3
88.9
85.89  104.66  17.50  0.89  2812  73.5%  33.0  124.7
57.5
34.5

Charging policy
Nearest
Fastest
MinChgOpT
DynaThreshold
CongestionAware
Nearest
Fastest
MinChgOpT
DynaThreshold
CongestionAware
Nearest
Fastest
MinChgOpT
DynaThreshold

CongestionAware  100.52  122.46  20.56  0.88  2760  88.6%  38.8

82
kWh

72
kWh

c. Impact of the number of fast and slower chargers

We further analyze the sensitivity of increasing the number of fast and slower chargers in the system for
c3000 (Table 10) and c4000 (Table 11) scenarios. The number of fast and slow chargers is increased from

24

12 chargers (6 fast and 6 slow) to 20 (10 fast and 10 slow) on the same charging stations (i.e. from 3
fast/slow chargers to 5 fast/slow chargers per charging station). The battery size is 62kWh and the other
parameters are identical as described in Section 4.1. For the c3000 scenario, increasing the number of
chargers  in  the  system  does  reduce  the  charging  congestion  for  the  benchmark  policies.  The  profit,
service rate, and charged amount of energy increase along with more fast and slow chargers in the system.
The  service  rate  increases  around  3%  if  the  number  of  chargers  is  increased  from  12  to  20.  For  the
CongestionAware policy, the benefit is less significant in terms of customer service rate and total system
profit  although  the  total  charging  waiting  time  decreases  accordingly  when  the  number  of  chargers
increases. For the c4000 scenario, using the benchmark policies results in a significant reduction in total
(charging) waiting time (see TW column in Table 11) when increasing the number of chargers from 12 to
16  (i.e.  from  -31%  to  -58%).  Adding  more  chargers  from  16  to  20  chargers  does  further  reduce  total
waiting time but is less effective (i.e. from 18% to -44%). The profit (+3.3 to +7.7%) and service rate (+2.1
to +6.2%) increase accordingly due to total waiting time reduction when the number of chargers increases
from 12 to 20. For the CongestionAware policy, the effectiveness of increasing the number of chargers
becomes much more significant than the benchmark. The profit and service rate are increased by 11.1%
(from  88.08k  to  97.81k)  and  9.8%  (from  76.5%  to  86.3%),  respectively  if  the  number  of  chargers  is
changed from 12 to 20. Interestingly, we observe that total charging time is reduced slightly from 48.4
hours  (12  chargers)  to 43.5  hours  (20  chargers),  but  the total  charged  amount  of  energy  is  increased
significantly from 3280kWh to 4467 kWh (+36.2%). In practice, the operator can further invest in their
charging infrastructure to increase the system's profitability.

Table 10. System performance for different numbers of fast and slow chargers (c3000 scenario).

# of
chargers
12

16

20

PF

TR

CC

TTC

ENG

SR  KMT

Charging policy

TC
TW
94.1
Nearest  73.02  88.93  14.72  0.89  2824  84.9%  27.8  111.7
94.1
94.0
Fastest  73.46  89.52  14.83  0.92  2935  85.7%  28.0
92.6
77.1
MinChgOpT  74.45  90.67  15.02  0.94  3011  86.9%  28.3
97.2  107.8
DynaThreshold  75.08  92.06  15.31  1.06  3430  88.7%  28.9
36.0
CongestionAware  80.59  97.93  16.07  0.80  2556  95.7%  30.3
52.4
Nearest  74.82  91.24  15.13  1.02  3264  87.6%  28.5
68.4  113.3
Fastest  75.63  92.24  15.28  1.03  3298  88.7%  28.8
46.2  106.6
MinChgOpT  76.69  93.56  15.52  1.09  3516  90.3%  29.3
31.6  105.8
DynaThreshold  76.55  93.99  15.61  1.24  4016  90.8%  29.5
54.8  126.2
CongestionAware  80.35  97.66  16.09  0.82  2579  95.3%  30.4
51.9
20.9
Nearest  75.60  92.18  15.28  1.03  3283  88.6%  28.8
43.8  120.7
Fastest  76.39  93.19  15.44  1.06  3414  89.9%  29.1
28.5  111.3
MinChgOpT  77.73  94.87  15.72  1.15  3756  91.8%  29.7
19.6  106.5
DynaThreshold  77.26  95.00  15.77  1.38  4443  92.0%  29.8
36.1  141.3
CongestionAware  80.66  98.03  16.12  0.84  2616  95.7%  30.4
52.5
10.1

Table 11. System performance for different numbers of fast and slow chargers (c4000 scenario).

# of
chargers
12

16

TR

CC

TTC

SR  KMT

Charging policy

PF
Nearest  76.55
Fastest  77.31
MinChgOpT  77.56
DynaThreshold  80.98

TC
TW
ENG
93.1
93.12  15.54  0.82  2657  64.2%  29.3  136.1
93.0
94.07  15.69  0.84  2745  64.8%  29.6  100.4
94.37  15.75  0.85  2796  65.1%  29.7
93.0
99.2
99.41  16.62  1.15  3751  68.6%  31.4  135.7  120.3
68.5
48.4
85.5  103.0
69.7  103.8
41.8  101.6

CongestionAware  88.08  107.64  17.95  1.04  3280  76.5%  33.9
95.17  15.89  0.82  2752  65.6%  30.0
96.62  16.14  0.88  2953  66.6%  30.5
98.30  16.42  0.93  3126  67.9%  31.0

Nearest  78.26
Fastest  79.38
MinChgOpT  80.74

25

20

DynaThreshold  84.98  104.25  17.44  1.25  4151  72.4%  32.9
CongestionAware  92.46  113.15  18.92  1.20  3753  80.6%  35.7
96.15  16.05  0.83  2796  66.3%  30.3
97.82  16.35  0.90  3038  67.6%  30.8
99.35  16.59  0.92  3138  68.7%  31.3
DynaThreshold  87.23  107.02  17.92  1.30  4366  74.8%  33.8
CongestionAware  97.81  120.01  20.07  1.43  4467  86.3%  37.9

Nearest  79.08
Fastest  80.35
MinChgOpT  81.66

74.8  137.5
45.3
75.4
70.3  112.2
45.3  106.6
23.6  104.7
43.0  145.8
89.9
43.5

Note that the day-ahead charging plan model P1 can be solved efficiently using a commercial solver to
obtain good approximate solutions given a reasonable computational time limit when the problem size
is  not  too  large.  For  our  computational  study,  we  use  a  one-hour  computational  time  limit,  and  the
obtained solutions have gaps to the lower bound from around 10% to 14% for the c3000 scenario and
around 5% for the c4000 scenario. When the problem size (in terms of the number of customers, vehicles,
and fast/slow chargers) increases, we can reduce the computational time by decomposing it into smaller
problem-size blocks with proportional customer demand, number of vehicles, and number of chargers in
the system to obtain a charging plan for the vehicles of the block and replicate it for the vehicles of the
others blocks. Another option is developing efficient heuristics to get good solutions, which remains a
future research avenue of this study.

d. Impact of overnight charging costs and different prices for the use of fast and slow chargers

level  2  charger

As shown in Figures 5 and 6, applying the CongestionAware charging policy results in lower SoC at the
end of the day, which requires overnight charging to restore 100% battery level for the start of service on
the following day. While overnight charging costs are lower, they may reduce the operator’s total profit.
For a fair comparison, we include overnight charging costs for each charging policy and recalculate the
profit and charging costs for c3000 and c4000 scenarios (i.e., recharge each vehicle from its SoC at the
end of the day (00:00) to 100% to get the overnight charging costs). For a level 2 charger in NYC, the
charging cost is $2.5 per hour from 6 am-9 pm and $1 per hour for overnight charging4. The standard
is  6.24kW 5  in  NYC,  so  we  estimate  the  charging  costs  as
power  of  a
$2.5/6.24kWh=$0.4/kWh during the day and $1/6.24kWh=$0.16 kWh for overnight charging. Note that
we assume that vehicles can be recharged to full during 0:00-6:00 (6 hours), based on vehicle battery size
and charging power of level 2 charger (assumed 11kW for our numerical studies). The results are shown
in Table 12. We can find that  for both scenarios, the CongestionAware policy has a higher  amount of
charged  energy  (also  higher  charging  costs)  over  a  24-hour  period  (including  overnight  charging)
compared with the other benchmark policies due to a higher customer service rate and KMT traveled.
However,  the  total  charging  costs  of  the  CongestionAware  are  compensated  by  higher  revenue  from
serving more customers, resulting in higher profit than the other benchmarks reported. As the cost for
overnight charging is much lower, incorporating this charging cost slightly reduces the total profit. The
same  conclusion  can  be  drawn  if  incorporating  the  overnight  charging  costs  for  the  other  numerical
studies in this Section.

Table 12. Comparison of the KPIs for different charging policies with and without overnight charging.

Scenario

Charging policy

c3000

Nearest
Fastest

PF

Without
o.c.
73.02
73.46

With
o.c.
72.34
72.78

6:00-
24:00
0.89
0.92

CC
0:00-
6:00
0.68
0.67

ENG
Total  6:00-
0:00-
6:00
24:00
2824  4262  7085
2935  4207  7142

1.57
1.59

Total

aSoC
(kWh)

19.4
19.9

4 Curbside Level 2 Charging Project FAQ. https://www.nyc.gov/html/dot/downloads/pdf/curbside-level-2-charging-pilot-
faq.pdf
5 https://www.flo.com/new-york-city/

26

(3000
requests)

MinChgOpT
DynaThreshold
  CongestionAware

73.77
74.43
79.75
75.79
76.55
76.80
80.27
87.20
Remark: o.c.: overnight charging (i.e., from 0:00-06:00). aSoC: Average SoC/vehicle at the end of the day.

3011  4198  7208
3430  4078  7508
2556  5243  7799
2657  4770  7428
2745  4765  7510
2796  4734  7529
3751  4404  8154
3280  5458  8738

Nearest
Fastest
MinChgOpT
DynaThreshold
CongestionAware

74.45
75.08
80.59
76.55
77.31
77.56
80.98
88.08

1.61
1.71
1.64
1.58
1.60
1.61
1.85
1.91

0.94
1.06
0.80
0.82
0.84
0.85
1.15
1.04

0.67
0.65
0.84
0.76
0.76
0.76
0.70
0.87

c4000
(4000
requests)

20.0
21.2
9.6
14.3
14.4
14.7
18.0
7.4

We further evaluate the performance of the proposed charging strategy with energy prices depending
on the types of chargers used. Charging costs using public fast and slow chargers in NYC are very similar:
for DC fast chargers, it is $0.39 per kWh consumed. Users need to pay the parking fee at the facility, but
the  first  hour  parking  fee  is  deducted  from  the  charging  transaction 6;  while  the  charging  costs  are
$0.4/kWh during the day for a level 2 slow charger. As the charging costs are usually much higher for DC
fast chargers, we assume the charging costs on a DC charger per kWh is double ($0.8/kWh) that of a slow
charger  ($0.4/kWh),  independent  of  day/overnight  charging.  Table  13  shows  the  results.  The
CongestionAware policy has the lowest waiting times and charging times compared with the benchmark
policies,  resulting  in  the  highest  customer  service  rate  and  profit.  The  results  indicate  that  the
CongestionAware  policy  systematically  outperforms  the  benchmark  approaches  for  c3000  and  c4000
scenarios when applying charger-type-specific charging costs.

Table 13. Comparison of the KPIs for different charging policies with doubled charging costs for the use
of DC fast chargers.
Scenario

ENG

c3000
(3000
requests)

c4000
(4000
requests)

SR

CC

TTC

Charging policy
Nearest
Fastest
MinChgOpT
DynaThreshold

PF
71.84
72.15
72.76
73.45
  CongestionAware  79.08
76.00
76.31
76.75
78.97

TC
TR
KMT
92.6
88.86  14.73  2.00  2762  84.9%  27.8
93.2
89.39  14.80  2.13  2908  85.5%  27.9
90.19  14.94  2.20  2987  86.4%  28.2
93.1
91.86  15.26  2.52  3426  88.3%  28.8  105.7  107.9
51.2
34.0
97.59  16.02  2.02  2524  95.3%  30.2
95.7
93.77  15.64  1.91  2689  64.6%  29.5  136.2
94.8
94.28  15.73  2.02  2795  65.0%  29.7  115.8
94.96  15.84  2.14  2943  65.5%  29.9
97.0
99.5
98.80  16.50  2.65  3652  68.1%  31.1  143.9  120.3
68.4

Nearest
Fastest
MinChgOpT
DynaThreshold
CongestionAware  86.51  107.59  17.95  2.58  3244  76.3%  33.9

TW
91.2
90.4
81.0

46.7

e. Charging station availability and imbalanced number of fast and slow chargers

This section aims to evaluate the effect of extreme charging station availability and demand variability on
the  performance  of  different  charging  policies,  including:  i)  extremely  low/high  charging  station
availability; ii) imbalanced number of fast and slow chargers; iii) variation of customer demand. We design
three scenarios as detailed in Table 14. The computational time details are reported in Appendix B.

Table 14. Scenarios for the system evaluation with different charging station availability and imbalanced
numbers of fast and slow chargers and customer demand variation.
Scenario   Description

Fleet size

Tested values
Demand (number of
requests/day)

Number  of  fast
slow
and

6 DC Fast Charging Station FAQ. https://www.nyc.gov/html/dot/downloads/pdf/dc-fast-charging-station-faq.pdf

27

100

100

3000

3000

chargers
slow)

(fast,

(2,2),(20,20)

(2,10), (4,20)

100

1000,2000,3000,4000,5000,6000

(6,6)

1

2

3

Charging
station
availability
Imbalanced
numbers of
fast and slow
chargers
Variation of
customer
demand

Remark: Battery size = 62 kWh. The number and location of fast and slow charging stations remain the same (2 fast
and 2 DC fast charging stations (see Figure 1) with balanced numbers of chargers). The other parameters are based
on Table 2.

Scenario 1

We solve the day-ahead charging schedule planning problem with one-hour computational time to obtain
a good solution. The computational time and gaps to the lower bound are reported in Appendix B. For
the case of extremely low numbers of chargers (2 fast and 2 slow), we cannot obtain a feasible solution
for the fleet size of 100 vehicles. Consequently, we reduce the number of vehicles for P1 gradually (reduce
10 vehicles at a time) to obtain feasible solutions for at most 50 vehicles. The remaining 50 vehicles go to
recharge when idle and their SoCs are below the threshold 𝜃 (Step 9 in Algorithm 1). The performance of
the  CongestionAware  and  other  benchmark  charging  policies  is  shown  in  Table  15.  As  expected,  the
results  demonstrate  that  the  CongestionAware  policy  outperforms  the  benchmark  more  significantly
when  the  availability  of  charging  facilities  is  low  (+4.71%  total  profit  compared  to  the  second-best
benchmark). The total waiting time for the benchmark policies are extremely high (more than 270 hours
in  total)  when  vehicles’  charging  operations  are  not  well  coordinated  to  avoid  peak  congestions  or
𝑚𝑎𝑥 (i.e.  80%);  while  the  CongestionAware  policy  avoids  recharging  vehicles
myopically  charging  to 𝐸𝑣
during charging peak hours with a partial recharge policy, resulting in significantly lower charging waiting
time  (14.2  hours  in  total).  On  the  other  hand,  when  the  fast  and  slow  chargers  are  abundant,  the
CongestionAware policy is slightly better than the MinChgOpT (+1.49% total profit). The gain in charging
waiting time is less significant compared with the MinChgOpT.

Table 15. System performance of different charging policies with an extremely low/high number of fast
and slow chargers.
# of
chargers1
(2,2)

Charging policy

PF
Nearest  64.09
Fastest  64.00
MinChgOpT  64.18
DynaThreshold  63.86
  CongestionAware  67.20
Nearest  74.74
Fastest  77.40
MinChgOpT  79.13
DynaThreshold  78.41
  CongestionAware  80.31

TR

CC

TTC

SR  KMT

TC
TW
ENG
35.4
77.55  12.78  0.34  1087  73.1%  24.1  274.8
34.9
77.46  12.78  0.34  1092  73.1%  24.1  270.9
34.9
77.66  12.81  0.34  1096  73.4%  24.2  271.4
42.7
77.89  12.87  0.41  1331  73.5%  24.3  313.1
14.2
80.94  13.32  0.28
18.2
881  77.2%  25.1
24.8  127.5
91.04  15.09  0.95  3032  87.2%  28.5
13.0  112.1
94.53  15.68  1.14  3709  91.4%  29.6
96.55  15.99  1.21  3997  93.8%  30.2
94.1
13.5  135.5
96.44  16.01  1.47  4803  93.6%  30.2
50.3
0.2
97.54  16.05  0.78  2513  95.2%  30.3

1.8

(20,20)

Remark: (fast, slow)

Scenario 2

28

This scenario considers the case with relatively low availability of fast chargers. We solve P1 with a 1-hour
computational  time  to  obtain  a  good  charging  schedule  for  the  fleet.  The  KPIs  of  different  charging
policies are shown in Table 16. The results show that the CongestionAware policy has the highest total
profit and customer service rate. When  doubling the number of both types of chargers, the customer
service rate of the CongestionAware policy is improved from 79.3% to 87.2%, resulting in a profit increase
of  8.27%.  The  total  waiting  time  and  charging  costs  are  reduced  significantly  for  the  benchmark
approaches with doubled chargers, but remain much higher than the CongestionAware policy. The profit
of the CongestionAware policy is higher than the benchmark approaches.

Table 16. System performance for different charging policies with an imbalanced number of fast and slow
chargers.
# of
chargers1
(2,10)

Charging policy

SR  KMT

CC

TR

PF
Nearest  66.44
Fastest  66.14
MinChgOpT  66.44
DynaThreshold  67.62
  CongestionAware  68.79
Nearest  71.37
Fastest  71.36
MinChgOpT  71.82
DynaThreshold  73.45
  CongestionAware  74.48

TTC

TC
TW
ENG
97.0
80.56  13.31  0.55  1751  76.1%  25.1  181.7
94.0
80.23  13.25  0.54  1734  75.7%  25.0  186.1
80.54  13.28  0.54  1743  76.1%  25.1  185.9
93.8
82.55  13.69  0.65  2104  78.1%  25.8  183.6  114.6
20.2
83.00  13.65  0.35  1108  79.3%  25.7
23.1
53.8  158.2
86.89  14.37  0.91  2863  82.7%  27.1
74.6  143.8
86.95  14.39  0.91  2872  82.8%  27.1
67.9  135.9
87.46  14.47  0.91  2863  83.3%  27.3
48.8  176.9
89.99  14.95  1.06  3427  86.1%  28.2
36.5
26.8
90.26  14.91  0.55  1754  87.2%  28.1

(4,20)

Remark: (fast, slow)

Scenario 3
In this scenario, we vary daily customer demand from 1000 to 6000 with an interval of 1000 customers.
As for the previous scenarios, a fleet of 100 vehicles with a 62 kWh battery is considered. The charging
facility has 6 fast and 6 slow chargers. For low-demand cases with 1000 and 2000 customers/day, there
are no charging operations scheduled from P1 (CongestionAware). The total charging time and energy of
the CongestionAware policy is a small fraction of the other benchmark approaches.  The profits of the
CongestionAware policy for the low-demand cases are similar to the benchmark policies (see Table 17).
However, for higher customer demand cases (from 3000 to 6000 customers/day), the CongestionAware
policy systematically outperforms the benchmark approaches with the least waiting times and the highest
profit (see Table 17 and Figure 11). Note that the location of charging stations may affect the access costs
of charging operations. The sensitivity analysis related to the impact of charging station locations remains
for future extensions of this study.

SR

c1000*

Table 17. Comparison of the KPIs for different charging policies for low customer demand.
KMT
TR
Scenario
9.9
33.27
9.9
33.27
9.9
33.27
9.9
33.26
33.27
9.9
66.02  10.68  0.59  1832  96.8%  20.2
66.18  10.72  0.59  1866  97.0%  20.2
66.22  10.71  0.59  1860  97.1%  20.2
65.83  10.68  0.66  2092  96.4%  20.2
390  95.6%  19.9
65.22  10.54  0.13

PF
Charging policy
27.96
Nearest
27.95
Fastest
27.95
MinChgOpT
27.78
DynaThreshold
CongestionAware  28.03
54.56
Nearest
54.63
Fastest
54.74
MinChgOpT
DynaThreshold
53.86
CongestionAware  54.49

ENG
173  97.1%
201  97.1%
204  97.1%
544  97.1%
2  97.1%

CC
TTC
5.24  0.05
5.24  0.06
5.24  0.07
5.24  0.16
5.24  0.00

c2000

TW
0.2
0.2
0.0
1.5
0.0
19.8
17.0
10.6
49.9
0.0

TC
8.8
4.8
4.4
13.2
0.0
62.0
55.5
47.4
63.2
7.8

29

c5000

c6000

75.43
76.65
77.00
81.38

Nearest
Fastest
MinChgOpT
DynaThreshold
CongestionAware  90.38  110.66  18.57  1.13  3568  60.2%  35.0
Nearest
Fastest
MinChgOpT
DynaThreshold
CongestionAware  91.49  111.92  18.73  1.16  3640  48.3%  35.3

85.5
91.56  15.35  0.65  2217  49.3%  29.0  108.5
86.0
95.8
93.12  15.61  0.70  2375  50.1%  29.5
93.55  15.69  0.72  2436  50.2%  29.6
85.9
82.2
99.67  16.70  1.04  3443  52.9%  31.5  144.7  117.0
72.2
50.7
89.1
91.71  15.38  0.67  2294  39.8%  29.0  137.6
87.8
92.79  15.56  0.70  2387  40.3%  29.4  125.9
89.1
93.69  15.71  0.74  2513  40.6%  29.7  117.5
99.78  16.71  0.96  3167  42.5%  31.5  133.2  109.7
73.5

75.53
76.38
77.10
81.75

47.1

Remark: cXX means XX requests. See Table 4 for the results of c3000 and c4000.

Figure 11. Profits of different charging policies with a variation of customer demand from 1000 to 6000
customers/day.

5. Conclusion and discussions

In this study, we develop an effective dynamic charging approach to coordinate vehicle dispatching and
charging operations for electric ride-hailing systems under stochastic demand, variable energy prices, and
congested  charging  stations.  We  focus  on  maximizing  the  total  system  profit  by  anticipating vehicles’
energy  needs  and  waiting  time  for  charging  on  different  chargers  during  the  day  to  reduce  vehicle
unavailability and increase the service rate of customers. The proposed sequential MILP approach first
determines  charging time and target SoCs of vehicles for a long planning horizon, based on which an
online reactive model optimizes vehicle-to-charger assignment for a short planning horizon to minimize
total  charging  operational  costs  given  the  current  system  state.  This  reactive  model  adjusts  vehicles’
charging  time  and  target  SoCs  after  recharge  based  on  vehicle’s  energy  needs  and  waiting  time  on
chargers for more effective utilization of congested charging stations. Four benchmark charging policies
are  used  to  compare  the  performance  of  the  proposed  method:  Nearest,  Fastest,  Minimum  charging
operational time, and dynamic hourly charging thresholds. We propose more realistic vehicles’ queuing
modeling at charging stations, i.e., no charging overlaps on each charger and maximum waiting time limits
in  a  queuing  charger.  A  more  realistic  minimum charging  time  requirement  per  charging  operation  is
considered in this study. To the best of our knowledge, it is still neglected in existing studies.

We conducted a simulation case study using NYC yellow taxi data in a Manhattan-like area with two
demand scenarios using a fleet of 100 EVs and limited fast and slow charging stations. The computational
results show that the developed methodology outperforms the benchmark approaches in terms of higher
profit and customer service rates under different scenarios. Overall, compared with the benchmark, the
proposed approach increases total profit by 7.65%-10.69% for the scenario of 3000 customers per day

30

and 8.76%-15.05% for that of 4000 customers per day. Similarly, the customer service rate is increased
by +7%-10.8% and +7.9%-12.3% for the c3000 and c4000 scenarios, respectively. When increasing the
battery  size  of  vehicles  and  the  number  of  chargers  in  the  system,  the  service  rate  could  be  further
improved from 76.5% (12 chargers  and 62kWh battery of vehicles) to 88.6%  (12 chargers and 82kWh
battery) and 86.3% (20 chargers and 62kWh battery) for the CongestionAware policy. Compared with the
benchmark, the CongestionAware policy increases the service rate systematically (up to +15.1%-16.2%
for the c4000 scenario with 12 chargers and 82kWWh battery). Moreover, the total charging waiting time
is significantly reduced compared with the benchmark. The proposed approach can be applied to support
transport  network  companies  for  more  efficient  charging  operation  management  under  limited
(congested) charging facilities under demand uncertainty.

Several  assumptions  and  limitations  of  our  proposed  approach  can  be  further  relaxed  through
additional  extensions.  First,  one  can  incorporate  overnight  charging  operations  into  the  day-ahead
charging schedule planning model, considering only charging at operator-owned charging stations or at
a  mixed  charging  infrastructure  involving  abandoned  public  charging  stations,  for  a  24-hour  planning
horizon.  This  enables  more  accurate  charging  operation  planning,  taking  into  account  heterogeneous
charging  station  capacity  constraints  during  both  the  day  and  overnight  periods.  Second,  if  we  allow
vehicles  to  recharge  at  public  charging  stations,  more  realistic  charging  cost  schemes  can  be  applied,
including  charger-type-specific  charging  fees  and  parking  costs.  This  would  enable  more  accurate
performance and sensitivity analysis under different charging policies and scenarios. Finally, in our test
instance generation, we randomly generate customers’ pickup and drop-off locations in the study area.
As NYC taxi data includes the exact pickup and drop-off taxi zones of trips, we can use this exact zone
data to generate random pickup and drop-off locations within these  zones. This would lead to better
transparency and make the comparison with other benchmarking studies more reliable.

Future  extensions  include  developing  efficient  solution  approaches  for  scaling  up  the  system,
applying this approach for optimizing vehicle battery configuration, fleet size, and charging infrastructure
planning,  etc.  Other  interesting  research  avenues  include  integrating  smart  charging  strategies  to
mitigate the impact of charging operations on the power grid during peak hours, extending this approach
for  different  systems  (e.g.,  shared  mobility  systems  or  regular  bus  services),  or  considering  dynamic
pricing to mitigate charging congestion. Incorporating different sources of uncertainty (e.g., stochastic
travel  times  or  traffic  congestion)  could  be  another  interesting  research  avenue  for  a  more  realistic
system performance evaluation.

Acknowledgments

The work was supported by the Luxembourg National Research Fund (C20/SC/14703944).

References

Abdullah, H.M., Gastli, A., Ben-Brahim, L., 2021. Reinforcement Learning Based EV Charging Management

Systems-A Review. IEEE Access 9, 41506–41531. https://doi.org/10.1109/ACCESS.2021.3064354

Ahadi,  R.,  Ketter,  W.,  Collins,  J.,  Daina,  N.,  2023.  Cooperative  Learning  for  Smart  Charging  of  Shared
Autonomous Vehicle Fleets. Transp. Sci. 57, 613–630. https://doi.org/10.1287/trsc.2022.1187
Al-Kanj, L., Nascimento, J., Powell, W.B., 2020. Approximate dynamic programming for planning a ride-
hailing  system  using  autonomous  fleets  of  electric  vehicles.  Eur.  J.  Oper.  Res.  284,  1088–1106.
https://doi.org/10.1016/j.ejor.2020.01.033

Bischoff, J., Maciejewski, M., 2014. Agent-based simulation of electric taxicab fleets. Transp. Res. Procedia

4, 191–198. https://doi.org/10.1016/j.trpro.2014.11.015

Dean,  M.D.,  Gurumurthy,  K.M.,  de  Souza,  F.,  Auld,  J.,  Kockelman,  K.M.,  2022.  Synergies  between
repositioning  and  charging  strategies  for  shared autonomous electric vehicle  fleets.  Transp.  Res.
Part D Transp. Environ. 108, 103314. https://doi.org/10.1016/j.trd.2022.103314

Farazi, P.N., Zou, B., Ahamed, T., Barua, L., 2021. Deep reinforcement learning in transportation research:
A review. Transp. Res. Interdiscip. Perspect. 11, 100425. https://doi.org/10.1016/j.trip.2021.100425
Froger,  A.,  Mendoza,  J.E.,  Jabali,  O.,  Laporte,  G.,  2019.  Improved  formulations  and  algorithmic
31

components  for the electric vehicle  routing problem with nonlinear charging functions. Comput.
Oper. Res. 104, 256–294. https://doi.org/10.1016/j.cor.2018.12.013

Iacobucci,  R.,  McLellan,  B.,  Tezuka,  T.,  2019.  Optimization  of  shared  autonomous  electric  vehicles
operations with charge scheduling and vehicle-to-grid. Transp. Res. Part C Emerg. Technol. 100, 34–
52. https://doi.org/10.1016/j.trc.2019.01.011

Jamshidi,  H.,  Correia,  G.H.A.,  van  Essen,  J.T.,  Nökel,  K.,  2021.  Dynamic  planning  for  simultaneous
recharging and relocation of shared electric taxis: A sequential MILP approach. Transp. Res. Part C
Emerg. Technol. 125. https://doi.org/10.1016/j.trc.2020.102933

Jenn, A., 2019. Electrifying Ride-sharing: Transitioning to a Cleaner Future [WWW Document]. UC Davis
Natl. Cent. Sustain. Transp. URL https://escholarship.org/uc/item/12s554kd (accessed 12.8.21).
Kullman,  N.D.,  Cousineau,  M.,  Goodson,  J.C.,  Mendoza,  J.E.,  2021.  Dynamic  Ride-Hailing  with  Electric

Vehicles. Transp. Sci. 56, 775–794. https://doi.org/10.1287/trsc.2021.1042

Laha, A., Yin, B., Cheng, Y., Cai, L.X., Wang, Y., 2019. Game Theory Based Charging Solution for Networked
Electric  Vehicles:  A  Location-Aware  Approach.  IEEE  Trans.  Veh.  Technol.  68,  6352–6364.
https://doi.org/10.1109/TVT.2019.2916475

Ma,  T.-Y.,  2021.  Two-stage  battery  recharge  scheduling  and  vehicle-charger  assignment  policy  for
e0251582.

services.

PLoS

One

16,

dynamic
https://doi.org/10.1371/journal.pone.0251582

dial-a-ride

electric

Ma,  T.-Y.,  Xie,  S.,  2021.  Optimal  fast  charging  station  locations  for  electric  ridesharing  with  vehicle-
station  assignment.  Transp.  Res.  Part  D  Transp.  Environ.  90,  102682.

charging
https://doi.org/10.1016/j.trd.2020.102682

Maljkovic, M., Nilsson, G., Geroliminis, N., 2023. Hierarchical Pricing Game for Balancing the Charging of
Technol.  31,  2728–2743.

Trans.  Control

Syst.

IEEE

Ride-Hailing
https://doi.org/10.1109/TCST.2023.3286330

Electric

Fleets.

Pantelidis, T.P., Li, L., Ma, T.-Y., Chow, J.Y.J.J., Jabari, S.E.G., 2022. A Node-Charge Graph-Based Online
Carshare  Rebalancing  Policy  with  Capacitated  Electric  Charging.  Transp.  Sci.  56,  654–676.
https://doi.org/10.1287/trsc.2021.1058

Shi, J., Gao, Y., Wang, W., Yu, N., Ioannou, P.A., 2020. Operating Electric Vehicle Fleet for Ride-Hailing
Intell.  Transp.  Syst.  21,  4822–4834.

IEEE  Trans.

Services  with  Reinforcement  Learning.
https://doi.org/10.1109/TITS.2019.2947408

Taxi  &  Limousine  Commission,  2022.  CHARGED  UP!  TLC’s  Roadmap  to  Electrifying  the  For-Hire

Transportation Sector in New York City. https://doi.org/10.12968/S0261-2097(22)60151-5

Yan, P., Yu, K., Chao, X., Chen, Z., 2023. An online reinforcement learning approach to charging and order-
dispatching optimization for an e-hailing electric vehicle fleet. Eur. J. Oper. Res. 310, 1218–1233.
https://doi.org/10.1016/j.ejor.2023.03.039

Yang,  Z.,  Guo,  T.,  You,  P.,  Hou,  Y.,  Qin,  S.J.,  2019.  Distributed  approach  for  temporal-spatial  charging
Informatics  15,  3185–3195.

IEEE  Trans.

Ind.

coordination  of  plug-in  electric  taxi  fleet.
https://doi.org/10.1109/TII.2018.2879515

Yi,  Z.,  Smart,  J.,  2021.  A  framework  for  integrated  dispatching  and  charging  management  of  an
autonomous  electric  vehicle  ride-hailing  fleet.  Transp.  Res.  Part  D  Transp.  Environ.  95,  102822.
https://doi.org/10.1016/j.trd.2021.102822

Yu, M., Hong, S.H., 2017. Incentive-based demand response considering hierarchical electricity market: A
267–279.

Energy

game

Appl.

203,

Stackelberg
https://doi.org/10.1016/j.apenergy.2017.06.010

approach.

Zalesak,  M.,  Samaranayake,  S.,  2021.  Real  time  operation of  high-capacity electric  vehicle  ridesharing
fleets. Transp. Res. Part C Emerg. Technol. 133, 103413. https://doi.org/10.1016/j.trc.2021.103413
Zhang, Q., Sun, T., Ding, Z., Li, C., 2021. Nodal dynamic charging price formulation for electric vehicle
through  the  Stackelberg  game  considering  grid  congestion.  IET  Smart  Grid  4,  461–473.
https://doi.org/10.1049/stg2.12025

Zhang,  R.,  Rossi,  F.,  Pavone,  M.,  2016.  Model  predictive  control  of  autonomous  mobility-on-demand
systems, in: 2016 IEEE International Conference on Robotics and Automation (ICRA). IEEE, pp. 1382–
1389. https://doi.org/10.1109/ICRA.2016.7487272

32

Appendix A. Comparison of different modeling approaches for vehicle queuing at chargers for
the benchmark charging policies.

In  the  literature,  existing  studies  assume  a  simplified  vehicle  queuing  behavior  modeling  at
chargers/charging stations, i.e., vehicles wait in a queued charger/charging station for charging without
time limits. This might not be realistic when the vehicle’s queuing times are very long (e.g., several hours).
In  this  case,  drivers  (vehicles)  might  prefer  to  move  to  other  nearby  chargers  or  least-waiting-time
chargers to recharge and return to serve customers earlier. To investigate the impact of queuing behavior
at chargers, three modeling approaches are tested as follows. Note that vehicles’ charger assignments
are determined by the applied charging policies.

a.  Naïve queuing: Vehicles wait in a queue for their target(assigned) charger without a time limit.
b.  Charger-chasing A: Vehicles wait at a charger (current charger) with a maximum waiting time of 15
minutes, then move away to a fast charger (next charger) with the least waiting time when arriving
at chargers’ locations. If vehicles cannot reach the next charger due to insufficient SoCs, vehicles go
to the closest charger to recharge. If unable to reach the closest one, vehicles wait at the current
charger until its turn.

c.  Charger-chasing B: Different from charger-chasing A, vehicles go to a fast or slow charger with the

least waiting time when moving away from the queue on current chargers.

Table A1 reports the performance of using different vehicle queuing modeling approaches. The upper
block in Table A1 is related to the c3000 scenario, while the lower block to the c4000 scenario. The results
show that using charger-chasing B has the highest service rates and profits for both demand scenarios.
The total waiting time at chargers using charger-chasing B is systematically lower than that of charger-
chasing A. However, using the naïve queue approach does not necessarily make it worse in terms of total
waiting time compared to the charger-chasing approach. It may depend on the applied charging policy
and uncertain queuing situations at chargers.

We further look into the details of the realized charging sessions for the c3000 scenario (The c4000
scenario has similar results; we neglect it here). Table A2 shows the results of using different queuing
modeling approaches for the benchmark charging policies for the c3000 scenario. When using the naïve
queuing approach, the number of realized charging operations is significantly  fewer than the charger-
chasing  approaches  due  to  the  long  waiting  time  on  queued  chargers.  The  charger-chasing  B  has  the
lowest average queuing time at chargers per charging session (5.55 minutes compared with the charger-
chasing A (6.15 minutes) and the naïve queuing (106.4 minutes). The average charged amount of energy
is similar. Still, the average charging times of charger-chasing B are higher than the charger-chasing B as
the latter considers both fast and slow chargers when vehicles go away from the current charger, resulting
𝑚𝑎𝑥.  Figure A1 reports the
in more utilization of slow chargers to charge from vehicles’ current SoC to  𝐸𝑣
boxplots for vehicle queuing time at chargers for realized charging sessions for the naïve queue and the
charger-chasing  B.  It  shows  that  using  the  naïve  queue  approach  might  result  in  an  unrealistic  long
queuing time for a charger while using the charger-chasing B would not have this issue.

33

Table A2. Effect of different modeling approaches for vehicle queuing at chargers.

Scenario

Queuing
approach

c3000

c4000

Naïve
queuing

Charger-
chasing
A

Charger-
chasing B

Naïve
queuing

Charger-
chasing
A

Charger-
chasing B

Charging
policy
Nearest
Fastest
MinChgOpT
DynaThreshold
Nearest
Fastest
MinChgOpT
DynaThreshold
Nearest
Fastest
MinChgOpT
DynaThreshold

Nearest
Fastest
MinChgOpT
DynaThreshold
Nearest
Fastest
MinChgOpT
DynaThreshold
Nearest
Fastest
MinChgOpT
DynaThreshold

PF

TR

TTC

CC

ENG

SR  KMT

TW

TC

34.7
65.11  78.43  12.94  0.33  1049  74.1%  24.4
80.5
62.6
73.00  88.69  14.70  0.81  2603  84.8%  27.7  109.2
66.4
74.16  90.16  14.94  0.86  2775  86.4%  28.2
87.9
67.0
74.92  91.27  15.15  0.91  2955  87.7%  28.6  120.5
94.1
73.02  88.93  14.72  0.89  2824  84.9%  27.8  111.7
73.1
73.11  89.07  14.77  0.86  2774  85.1%  27.9  125.2
70.6
73.89  89.95  14.90  0.87  2807  86.2%  28.1  103.8
71.3
74.28  90.99  15.11  0.96  3112  87.4%  28.5  137.8
94.1
73.02  88.93  14.72  0.89  2824  84.9%  27.8  111.7
94.1
94.0
73.46  89.52  14.83  0.92  2935  85.7%  28.0
77.1
74.45  90.67  15.02  0.94  3011  86.9%  28.3
92.6
97.2  107.8
75.08  92.06  15.31  1.06  3430  88.7%  28.9

65.96  79.63  13.26  0.36  1160  55.4%  25.0
96.7
37.6
76.34  92.83  15.50  0.81  2641  64.0%  29.2  122.1
63.9
77.83  94.63  15.80  0.84  2714  65.2%  29.8
87.0
69.5
80.45  98.25  16.44  1.04  3390  67.8%  31.0  182.7
80.5
76.55  93.12  15.54  0.82  2657  64.2%  29.3  136.1
93.1
76.07  92.55  15.44  0.81  2643  63.8%  29.1  138.3
73.2
77.01  93.69  15.63  0.84  2740  64.7%  29.5  126.3
74.0
78.92  96.99  16.22  1.09  3564  66.7%  30.6  170.3
89.9
76.55  93.12  15.54  0.82  2657  64.2%  29.3  136.1
93.1
77.31  94.07  15.69  0.84  2745  64.8%  29.6  100.4
93.0
93.0
99.2
77.56  94.37  15.75  0.85  2796  65.1%  29.7
80.98  99.41  16.62  1.15  3751  68.6%  31.4  135.7  120.3

Table A2. Statistics of realized charging sessions for different modeling approaches for vehicle queuing
at chargers (c3000 scenario).

Queuing approach

Charging
policy

# of realized
charging
sessions

Naïve queuing

Charger-chasing A

Nearest
Fastest
MinChgOpT
DynaThreshold
Nearest
Fastest
MinChgOpT
DynaThreshold
Nearest
Fastest
MinChgOpT
DynaThreshold
Remark: Time is measured in minutes; energy is measured in KWh.

26
68
72
84
71
74
69
87
71
76
80
98

Charger-chasing B

Average
queuing
times per
charging
session
165.9
96.3
77.0
86.4
5.9
6.2
6.0
6.5
5.9
4.8
5.5
6.0

Average
charging times
per charging
session

Average
charged energy
per charging
session

81.0
59.5
58.4
49.5
80.8
64.6
60.9
48.9
80.8
75.8
73.6
67.4

38.8
40.3
39.9
36.0
39.4
39.4
41.0
36.6
39.4
39.9
39.6
36.6

34

Figure A1. Boxplots for vehicle queuing times at chargers of the realized charging sessions for the
benchmark charging policies. Naïve queueing (on the left) and charger-chasing B (on the right).

Appendix B. Impact of problem size on the computational times of different models (P1-P3) for the
CongestionAware policy.

In  this  appendix,  we  report  detailed  computational  times  for  solving  P1-P3  problems  of  the
CongestionAware policy and simulation times for the experiments in Section 4. To further evaluate the
computational bottleneck when scaling up the problem size in terms of the number of vehicles, number
of customers per day, and number of chargers, we generate four larger test datasets with the number of
customers  and  fleet  size  up  to  20000  customers/day  and  500  vehicles.  The  number  of  fast  and  slow
chargers  is  increasing  accordingly  (over  the  four  charging  stations).  For  each  dataset,  we  randomly
generate 15 test instances using the same approach (Section 4.1) in which 10 test instances are used to
estimate the model parameters and the remaining 5 test instances are used to evaluate the performance
of the different charging policies. The characteristics of the larger test datasets are shown in Table B1.

Table B1. Characteristics of the four larger test datasets.

Demand
(number of
request/day)
8000
1200
16000
20000

Fleet
size

200
300
400
500

Battery (kWh)

|𝑆𝑓𝑎𝑠𝑡|

|𝑆 𝑠𝑙𝑜𝑤|

62
62
62
62

12
18
24
30

20
30
40
50

Remark: Battery size = 62kWh. The number and location of fast and slow charging stations remain the
same (2 fast and 2 DC fast charging stations).  The other parameters are based on Table 2.

Table B2 reports the CPU time (in seconds) and the relative gaps to the lower bound for solving the P1
problem. We use a one-hour computational time to solve approximately P1 for the computational studies
in Section 4. The relative gaps range from around 2% to 19.55%. We can observe that given the same
number of customer demand and fleet size to schedule, the availability of chargers has significant impact
on the gaps to the lower bound, given same computational time limits, in particular when the number of
chargers are extremely low/high. For larger test datasets, we report the gaps to the lower bound with 1,
2 and 4 hours computational time. The results show that the gaps can be reduced significantly during the
first 2 hours and then reach around 8-14% with a slower reducing speed. Note that given an unknown

35

and  stochastic  customer  demand,  the  day-ahead  charging  schedule  P1  aims  to  obtain  approximate
charging schedules for the fleet to determine where and how much energy to charge, given the operator’s
available computational time and resource limits.

Table B2. CPU times and gaps to the lower bounds for solving P1 for the computational studies in
Section 4 and larger test datasets.

# of
requests

1000
2000
3000
3000
3000
3000
3000
3000
4000
4000
4000
5000
6000
8000
12000
12000
12000
16000
16000
16000
20000
20000
20000

𝑉

100
100
100
100
50*
100
100
100
100
100
100
80*
70*
200
300
300
300
400
400
400
500
500
500

Battery
(kWh)

|𝑆𝑓𝑎𝑠𝑡|

|𝑆 𝑠𝑙𝑜𝑤|

62
62
62
62
62
62
62
62
62
72
82
62
62
62
62
62
62
62
62
62
62
62
62

6
6
6
6
2
20
2
4
6
6
6
6
6
12
18
18
18
24
24
24
30
30
30

6
6
6
6
2
20
10
20
6
6
6
6
6
20
30
30
30
40
40
40
50
50
50

∆ℓ

30
30
30
20
30
30
30
30
20
20
20
20
20
20
20
20
20
20
20
20
20
20
20

CPU
(sec.)

0
0
3600
3600
3600
3600
3600
3600
3600
3600
3600
3600
3600
3600
3600
7200
14400
3600
7200
14400
3600
7200
14400

Gap to
lower
bound
0.00%
0.00%
13.97%
11.27%
19.55%
4.62%
15.83%
11.51%
5.24%
9.88%
5.32%
4.32%
2.01%
8.13%
12.00%
8.74%
8.73%
14.90%
11.30%
11.19%
41.00%
17.50%
14.12%

Remark: The fleet size that can be solved to obtain feasible solutions, given the energy consumption rate, the
battery size of vehicles, and the number of fast and slow chargers for that test instance. We set ∆ℓ=20 for the
problem with a number of customers greater than 3000, instead of 30 minutes, to obtain feasible solutions.

Table  B3  reports  the  CPU time  to  solve  vehicle  dispatching  (every  minute)  and online  vehicle-charger
assignment (see  Algorithm 1)  for different test  instances with the number of customers ranging from
3000/day  to  20000/day.  For  the  c3000  to  c6000  test  instance,  the  fleet  size  is  100  vehicles,  and  the
number of fast and slow chargers is 6 each. The setting for c8000-c20000 is shown in Table B1. For c3000,
the average number of customers |𝑅𝑡| and vehicles |𝑉𝑡| is 5.0 and 42.9, respectively; while for c20000,
|𝑅𝑡| and |𝑉𝑡| become 58.2 and 165.5, respectively. The standard deviations are relatively high for both
variables,  too.  The  average  CPU  time  is  0.0011  seconds  for  c3000  and  0.0221  seconds  for  c20000,
respectively,  fast  enough  for  real-time  applications  with  the  problem  size  of  P1  up  to  hundreds  of
customers and hundreds  of vehicles  to dispatch. For P3, the  problem size depends on the number of
vehicles |𝑉𝑡| (changing over time) and that of chargers |𝑆| (fixed). For the largest case of c20000, |𝑆| is
80,  and  the  average  and  standard  deviation  of |𝑉𝑡| are  38.4  and  23.1,  respectively.  The  average  and
standard deviation of the CPU time are 0.0082 and 0.0109 seconds, respectively, showing that solving the
P3 problem is very fast, suitable for real-time applications.

36

Table B3. Problem size and CPU times for solving P2 (vehicle dispatching) and P3 (online vehicle-charger
assignment) for different test instances.
𝑃2

𝑃3

# of
requests

c3000
c4000
c5000
c6000
c8000
c12000
c16000
c20000

|𝑅𝑡|

|𝑉𝑡|

avg.
5.0
13.6
24.0
34.5
26.0
36.8
48.7
58.2

s.d.
2.9
11.4
15.9
18.0
23.9
34.8
44.9
53.8

avg.
42.9
33.1
29.6
29.2
65.7
100.0
133.7
165.5

s.d.
15.9
19.0
20.8
21.3
34.1
52.8
71.3
86.5

CPU (sec.)
avg.

s.d.
0.0011  0.0039
0.0014  0.0043
0.0016  0.0045
0.0018  0.0048
0.0037  0.0067
0.0074  0.0085
0.0117  0.0112
0.0221  0.0179

|𝑆|

|𝑉𝑡|

avg.
5.9
6.9
7.0
7.0
16.4
23.7
32.0
38.4

12
12
12
12
32
48
64
80

CPU (sec.)
avg.
s.d.
2.1  0.0014
3.1  0.0005
3.2  0.0004
3.2  0.0004
9.0  0.0012
13.7  0.0023
18.5  0.0041
23.1  0.0082

s.d.
0.0044
0.0026
0.0024
0.0024
0.0041
0.0055
0.0072
0.0109

Table B4 further reports the number of times that P2 and P3 were evoked during the simulation when
solving a test instance in question. For P2, this number is bounded by the planning horizon (1080, one-
minute  decision  epoch  for  a  1080-minute  planning  horizon).  For  P3,  the  evoked  number  increases
exponentially with the problem size, depending on the scale and interactions of the charging supply and
demand.  As  shown  in  Algorithm  1  (Steps  11-13),  when  there  are  no  feasible  vehicle-to-charger
assignments, a series of attempts are executed by removing one vehicle with the highest SoC at a time
until feasible solutions are found. Table B5 reports the CPU time for running the simulation using different
charging policies for different test instances. For the CongestionAware policy, it takes around 20 minutes
to  finish  a  simulation  for  the  largest  c20000  test  instance.  Table  B6  reports  the  KPIs  using  different
charging policies for the larger test datasets. The results show that the CongestionAware systematically
outperforms the benchmark charging policies.

Table B4. The average number of executions for P2 and P3 for different test instances.
# of requests
c3000
c4000
c5000
c6000
c8000
c12000
c16000
c20000

𝑃3
539
3263
4251
4911
10854
15154
18982
24045

𝑃2
935
1041
1070
1067
1075
1079
1079
1079

Nearest

Fastest  MinChgOpT  DynaThreshold  CongestionAware

Table B5. Average computational time of one simulation run for different charging policies (in seconds).
 # of
requests
c1000
c2000
c3000
c4000
c5000
c6000
c8000
c12000
c16000
c20000

2.8
3.4
4.7
10.9
14.1
16.6
89.0
244.4
503.6
1283.7

1.5
2.0
2.7
4.7
9.3
12.4
21.6
51.8
85.0
154.3

1.5
1.9
2.2
3.7
6.5
9.3
16.2
37.1
71.8
121.6

1.5
2.2
2.5
4.8
9.0
12.1
22.0
50.8
86.5
155.7

2.3
2.7
3.6
5.2
9.6
12.8
23.1
55.2
89.1
175.3

37

Table B6. Comparison of the KPIs for different charging policies for larger test datasets.
Demand  Charging policy
c8000

TTC  CC  ENG

KMT

TR

SR

PF

TW

TC

Nearest  153.2  185.3  30.4  1.3
Fastest  156.3  189.1  31.1  1.4
MinChgOpT  158.5  191.8  31.5  1.5
DynaThreshold  167.0  203.2  33.6  2.0
  CongestionAware  178.0  216.6  35.7  2.0
Nearest  230.2  277.5  45.2  1.8
Fastest  234.6  283.1  46.1  2.0
MinChgOpT  237.7  286.8  46.7  2.0
DynaThreshold  251.5  305.3  50.0  2.8
  CongestionAware  271.3  329.1  53.6  3.0
Nearest  304.6  366.6  59.2  2.3
Fastest  312.0  375.7  60.7  2.6
MinChgOpT  316.4  381.1  61.6  2.7

4466  63.0%
57.4  137.7  203.7
4797  64.4%
58.6  109.3  192.3
5067  65.4%
59.5
86.3  186.7
6646  69.5%
63.3  120.4  263.9
6313  76.1%
91.3  126.3
67.3
6158  62.6%
85.2  161.1  287.5
6767  64.0%
87.0  144.5  285.9
6891  64.9%
88.1
95.2  257.7
94.4  132.5  368.8
9332  69.5%
9406  77.2%  101.1  117.9  188.5
7801  62.1%  111.7  219.3  379.4
8591  63.7%  114.6  170.8  365.6
99.3  327.4
8967  64.8%  116.3
DynaThreshold  331.6  401.5  65.2  3.5  11465  68.5%  123.0  154.9  470.2
  CongestionAware  363.4  440.2  71.2  3.9  12413  77.3%  134.3  146.2  248.3
9271  61.6%  138.6  219.0  446.6
9979  63.0%  141.6  162.2  421.8
MinChgOpT  391.9  471.2  75.8  3.0  10243  63.8%  143.0  108.4  388.1
DynaThreshold  414.7  501.0  80.8  4.2  13765  68.4%  152.4  203.5  565.7
  CongestionAware  461.9  558.6  89.6  5.0  15767  78.5%  169.0  166.3  315.3

Nearest  380.3  457.0  73.5  2.8
Fastest  388.1  466.6  75.0  3.0

c12000

c16000

c20000

38

