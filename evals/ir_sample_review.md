# IR eval set: hand-check sample

Seeded random sample (seed 20261022) of 20 labelled rows.
A row is **correct** if (1) the question is the intervenor's question, complete and not mixed
with another IR, (2) the response is Toronto Hydro's response to it, and (3) every gold exhibit
is cited in the response as a place where the answer/evidence is found.

Mark each `verdict:` as `correct` or `wrong (<reason>)`. `label-for-query:` records the looser question
that matters for the retrieval eval: do the gold exhibits locate the answer to the part of the question
that is actually in the query? Then run `uv run python -m evals.record_hand_checks`.

**Reviewed by Claude (claude-opus-5-5 in Claude Code), not a human**, on 2026-10-22, at the user's
request, after the multi-part and other-proceeding parser fixes. Each row was checked against the full
response text. The review of the previous eval set is kept in `evals/results/v1/ir_sample_review.md`.

## 1. 2B-VECC-18  (doc `rds-851961`, pp. 470-473)

- gold (response) exhibits: **1B, 4**
- reference-line exhibits: 2B
- PDF: http://localhost:3077/api/pdf/rds-851961#page=470

**Question (as filed)**

```
a) Presumably customers are concerned with the duration of outages irrespective of their
reason and especially if the outage is a matter within THESL’s ability to address. The PIM
measure for Outage Duration excludes Scheduled Outages. Why?
b) Are there any other measures used by THESL to gauge the response capability/efficiency of
outage recovery?
c) With respect to scheduled outages are planned projects provided guidelines or
expectations for maximum outage time? If so, please provide or explain the process that is
used to ensure that a given project meets the expected outage time.
```

**Query used for retrieval (locations stripped)**

```
a) Presumably customers are concerned with the duration of outages irrespective of their
reason and especially if the outage is a matter within THESL’s ability to address. The PIM
measure for Outage Duration excludes Scheduled Outages. Why?
b) Are there any other measures used by THESL to gauge the response capability/efficiency of
outage recovery?
c) With respect to scheduled outages are planned projects provided guidelines or
expectations for maximum outage time? If so, please provide or explain the process that is
used to ensure that a given project meets the expected outage time.
```

**Response**

```
Please refer to Exhibit 1B, Tab 3, Schedule 1, pages 8-9 for an explanation of the rationale behind
the PIM measures. Independent of the PIM measure, Toronto Hydro measures and monitors “all-
in” reliability metrics (including scheduled outages) on an ongoing basis, and has an established
process for managing the impacts of scheduled outages on customers.
Toronto Hydro agrees that customers are concerned about outages irrespective of their reason.
However, Toronto Hydro disagrees with the implication that scheduled outages are equivalent to
unplanned outages when it comes to the customer experience. Toronto Hydro offers the following
high-level comparison of scheduled and unplanned outages for further consideration.
Aspect
Scheduled Outages
Unplanned Outages
Predictability
Planned in advance,
scheduled time known
Occur without warning,
unpredictable
Duration and Impact
Typically short, a few hours,
and contained
Variable, can last from
minutes to days, and can
impact thousands of
customers
Aspect
Scheduled Outages
Unplanned Outages
No advance notice
Communication
Toronto Hydro communicates
schedule in advance
Impact on Customers
Predictable, can plan around
outage
Disruptive, can cause
inconvenience and losses
Mitigation Options
Customers can prepare, use
backup power
Limited options, may not be
able to mitigate
Frequency
Regular, scheduled based on
capital and maintenance plan
Occasional, based on system
reliability
Preventive Purpose
Preventive maintenance,
system improvements
Reactionary response to
failures

Toronto Hydro routinely measures and monitors “all-in” SAIFI and SAIDI, “defective equipment”
SAIFI and SAIDI, volume/impact of outages by specific cause codes and availability/accuracy of
outage Estimated Time of Restoration. Large outages are reviewed on a weekly basis for lessons
learned and improvement opportunities.

Crews undertaking scheduled outages are expected to plan outages in a manner that minimizes
customer impact (duration and scope) to the extent possible. Outage requests are submitted to the
Control Centre with start and finish times. Controllers will review the request and create a switching
order to enable work to be completed safely while minimizing the number of customers impacts.
Field Managers oversee the work and monitor progress to ensure that work is completed within the
allotted time.
Additionally, in the planning phase, proactive engagement with customers is facilitated through
community relations teams (as detailed in Exhibit 4, Tab 2, Schedule 18). Notices regarding power
interruptions, along with advance information about the expected outage duration, are provided.
RESPONSES TO VULNERABLE ENERGY CONSUMERS COALITION
INTERROGATORIES
```

verdict: correct
label-for-query: yes

## 2. 2B-DRC-11  (doc `rds-843534`, pp. 162-170)

- gold (response) exhibits: **2B, 1B**
- reference-line exhibits: 2B
- PDF: http://localhost:3077/api/pdf/rds-843534#page=162

**Question (as filed)**

```
THESL engaged Element Energy (“EE”) to develop the Future Energy Scenarios model report (the
“FES Report”) to offer a range of plausible trajectories on the path toward decarbonization.

a) Please place the TransformTO Net Zero Strategy materials on the record in this proceeding.
b) Please explain why THESL and/or EE chose the TransformTO scenarios and any advantages
or disadvantages in terms of the reliability of these scenarios for THESL over the next five
years.
c) Please discuss the implications of the four central scenarios in the FES Report specifically
for DERs, EVs, storage.
d) Please explain what the drivers are for EV transition in the steady progression scenario and
whether it’s a gradual or concentrated transition.
e) Please explain how THESL’s assumed EV adoption is aligned with TransformTO and why
that is the standard that TH adopted. As part of your response, please also discuss whether
any other metrics were considered by THESL and whether there are any disadvantages to
relying on a plan that was developed in 2020.
f) Please explain what the drivers are for solar power adoption in the steady progression
scenario and whether it’s a gradual or concentrated transition.
g) Please elaborate on the moderate increase anticipated in the System Transformation
scenario for distributed renewable generation.
h) Please discuss what would be involved in assessing the probability of any specific outcome
taking place.
i)
Please elaborate on drivers behind what THESL considers falling technology costs relevant
to the distributed renewable generation that was identified as a possibility in the FES
Report.
j)
Please explain how the scenarios capture “the impact of flexibility options such as energy
storage, smart charging and vehicle to grid options for electric vehicles”.
k) Please provide the full list of attributes used in the EE’s “Electric Car Consumer model” and
indicate which attributes THESL considers to be the most significant and describe how it
affects EV uptake.
l)
Please indicate whether THESL accepts that consumer preferences and related consumer
behaviour is changing and discuss how this and any such changing attitudes are
incorporated into the analysis performed in the FES Report?
m) Did EE consider any other comparable jurisdictions (USA, Europe)? If, yes please indicate
which jurisdictions and discuss how this was included in the analysis. If no, please discuss
why no other comparable jurisdictions were included in the analysis.
n) Please in
```

**Query used for retrieval (locations stripped)**

```
THESL engaged Element Energy (“EE”) to develop the Future Energy Scenarios model report (the
“FES Report”) to offer a range of plausible trajectories on the path toward decarbonization.
a) Please place the TransformTO Net Zero Strategy materials on the record in this proceeding.
b) Please explain why THESL and/or EE chose the TransformTO scenarios and any advantages
or disadvantages in terms of the reliability of these scenarios for THESL over the next five
years.
c) Please discuss the implications of the four central scenarios in the FES Report specifically
for DERs, EVs, storage.
d) Please explain what the drivers are for EV transition in the steady progression scenario and
whether it’s a gradual or concentrated transition.
e) Please explain how THESL’s assumed EV adoption is aligned with TransformTO and why
that is the standard that TH adopted. As part of your response, please also discuss whether
any other metrics were considered by THESL and whether there are any disadvantages to
relying on a plan that was developed in 2020.
f) Please explain what the drivers are for solar power adoption in the steady progression
scenario and whether it’s a gradual or concentrated transition.
g) Please elaborate on the moderate increase anticipated in the System Transformation
scenario for distributed renewable generation.
h) Please discuss what would be involved in assessing the probability of any specific outcome
taking place.
i)
Please elaborate on drivers behind what THESL considers 
```

**Response**

```
Please refer to the TransformTO Net Zero Strategy:
https://www.toronto.ca/legdocs/mmis/2021/ie/bgrd/backgroundfile-173758.pdf

As noted on page 3 of Section 2 of the FES report, the TransformTO scenarios were used as a
“reference point to define the overall level of ambition modelled in the four scenario worlds.” The
TransformTO inputs were complemented by numerous other inputs, including the scenario worlds
framework used by National Grid in the U.K., which defines scenario worlds according to their level
of societal change and speed of decarbonization. Ultimately, the final scenario worlds in the FES
model and report were shaped by internal stakeholder discussion and consensus, and did not
simply adopt the TransformTO scenarios without scrutiny. Toronto Hydro regards the modelled
scenarios as being reasonable and fit for the purpose of the exercise, which was to illustrate the
range of uncertainties in the low carbon energy transition.

These scenarios reinforce the fact that the rates of uptake of DERs, EVs, and storage are highly
uncertain and will depend on numerous economic and policy factors, which as a consequence,
creates uncertainty for system planning.

Please see Section 4.3 of the FES report for details regarding the electrification of transport.
Regarding the Steady Progression scenario world, Table 17 outlines how each of the modeled
parameters map to the scenario world. For example, the details and graphs which outline or refer
to the “Low” scenario in Section 4.3.2 detail the key inputs, methodology, and modeling that feed
into the EV transition, for cars and light trucks, in the Steady Progression scenario world.

Please see section 4.3.1 which outlines the modelling approach for EV adoption and states that
“Element Energy’s “Electric Car Consumer model” (ECCo) was used to generate bottom-up
technology uptake scenarios for cars and light trucks, which consist of a varying mixture of full
electric, hybrid and alternative-fuels based transport options.” As noted in the same section,
TransformTO data was used to derive an annual growth factor for the stock of cars and light trucks,
which was applied to the base year stock to give an absolute number of cars and light trucks in the
city each year; this feeds into the vehicle stock rather than the relative proportion or adoption of
EVs as part of that stock. Detailed further in Section 4.3.2, it is reiterated that a bottom-up
modelling approach was taken: “ECCo was used to model the development of the car stock from
the common starting point derived as described in Section 4.3.1. By varying the assumptions
related to policy, vehicles costs and infrastructure, three uptake scenarios for BEVs and PHEVs were
developed representing a range of ambition levels.”

Please see Section 4.4.2 of the FES report for the details regarding solar photovoltaics. Regarding
the Steady Progression scenario world in particular, Table 26 outlines how each of the modeled
parameters map to the scenario world
```

verdict: correct
label-for-query: yes

## 3. 2B-STAFF-186  (doc `rds-846609`, pp. 231-231)

- gold (response) exhibits: **2B**
- reference-line exhibits: 2B
- PDF: http://localhost:3077/api/pdf/rds-846609#page=231

**Question (as filed)**

```
Toronto Hydro states: “Toronto Hydro forecasts over 50 additional Energy Storage connections…to
the distribution system. This would increase…the total installed Energy Storage capacity to
89.5MW.”

Does Toronto Hydro anticipate that the total volume of energy storage connected to its system by
2029 will materially assist in mitigating customer outage durations associated with events caused
by freezing rain, windstorms or floods, i.e., similar to the events listed in the Extreme Weather and
Major Event Day sections of this application (e.g. Exhibit 1B Section 2.3.4, Exhibit 2B Section C2.3)?
Please explain.
```

**Query used for retrieval (locations stripped)**

```
Toronto Hydro states: “Toronto Hydro forecasts over 50 additional Energy Storage connections…to
the distribution system. This would increase…the total installed Energy Storage capacity to
89.5MW.”
Does Toronto Hydro anticipate that the total volume of energy storage connected to its system by
2029 will materially assist in mitigating customer outage durations associated with events caused
by freezing rain, windstorms or floods, i.e., similar to the events listed in the Extreme Weather and
Major Event Day sections of this application (e.g. , )?
Please explain.
```

**Response**

```
No. The non-wires solutions proposed for the 2025-2029 period are outlined in detail in Exhibit 2B
Section E7.2. Toronto Hydro intends to utilize DERs, including energy storage resources, as demand
response in a manner that is practical and prudent given the current availability of DER capacity,
and level of market maturity. At this time, Toronto Hydro is not utilizing customer-owned DERs to
manage grid outages. The use of customer-owned DERs for this purpose would require specific
connection arrangements and requires further study. Toronto Hydro will continue to explore such
use cases and determine whether they are practical or prudent.
Toronto Hydro’s ESS program targets the enablement of REG connections and does not
contemplate additional use cases to support the distribution system. Please see Exhibit 2B Section
7.2.2 for more details.
```

verdict: correct
label-for-query: yes

## 4. 2A-SEC-30  (doc `rds-843543`, pp. 41-42)

- gold (response) exhibits: **6**
- reference-line exhibits: 2A
- PDF: http://localhost:3077/api/pdf/rds-843543#page=41

**Question (as filed)**

```
SEC seeks to understand the revenue requirement impact of the proposal capital expenditures.
Please provide a table that shows for each year between 2025 and 2029, the revenue
requirements, broken down by component, related only to the proposed 2025 to 2029 capital
expenditures.
```

**Query used for retrieval (locations stripped)**

```
SEC seeks to understand the revenue requirement impact of the proposal capital expenditures.
Please provide a table that shows for each year between 2025 and 2029, the revenue
requirements, broken down by component, related only to the proposed 2025 to 2029 capital
expenditures.
```

**Response**

```
Table 1 below presents an estimate of 2025-2029 revenue requirement associated with 2025-2029
capital expenditures broken down by component. The revenue requirement provided below is
based on an estimate of the updated 2025-2029 total Revenue Requirement, which includes
impact from: (i) the 2023 actuals and updated 2024 forecast (presented in 2A-Staff-104), and (ii)
the January 29, 2024 evidence update. The final PILS models for the updated 2025-2029 total
Revenue Requirement (Exhibit 6) are not yet available because it was not possible to complete this
work within the timelines for responding to interrogatories. This information will be provided in
advance of the Technical Conference as indicated in 1A-Staff-01 and noted in the Application
Evidence Update cover letter.1
Table 1: 2025-2029 Estimated Capital-Related Revenue Requirement
2025
2026
2027
2028
2029
2025-2029
ROE
4.3
19.7
42.1
66.8
90.6
223.5
Deemed Interest
2.8
12.8
27.3
43.3
58.7
144.7
Depreciation
39.6
55.4
83.9
115.9
146.2
441.0
PILS
(0.3)
(12.0)
(29.5)
4.0
(2.9)
(40.7)
1 EB-2023-0195, Toronto Hydro 2025-2029 Custom Rate Application For Electricity Distribution Rates and
Charges – Evidence Update, January 29,2024, page 1.
Revenue Requirement
46.3
75.9
123.8
230.0
292.5
768.5
Rounding variances may exist
```

verdict: wrong (Exhibit 6 is cited as where updated figures are 'not yet available', not where the answer is)
label-for-query: no (same reason)

## 5. 5-STAFF-313  (doc `rds-851818`, pp. 156-159)

- gold (response) exhibits: **6**
- reference-line exhibits: 5, 1C
- PDF: http://localhost:3077/api/pdf/rds-851818#page=156

**Question (as filed)**

```
Toronto Hydro stated that is had an all-in coupon rate of 4.93% on Toronto Hydro Corporation’s
(THC) 30-year issuance on August 28, 2023. However, OEB staff could not find this bond listed in
Toronto Hydro’s Appendix OB Debt Instruments for the rate year 2025.
In Appendix OB, Toronto Hydro indicated that on October 2, 2023, it had issued a debenture for
$200,000,000 with a rate of 5.25%, however, no promissory note was filed in Toronto Hydro’s
evidence in Exhibit 1C. Also, “Table 5: Forecasted Long-Term Debt Issues” on page 6 of Exhibit 5
shows a forecasted rate of 5.00% and not 5.25% for the debt issued in October 2023.
The deemed long-term debt rate of 4.58% for electricity distributors was issued by the OEB on
October 31, 2023.
Toronto Hydro has calculated a long-term debt rate of 3.95% in Appendix OB for the 2025 rate
year. A long-term debt rate of 3.95% is also reflected in Toronto Hydro’s Excel revenue
requirement workforms for the rate years 2025 through 2029.

a) Please reconcile the debt that Toronto Hydro stated was issued on August 28, 2023 with
the debt issuances shown in Appendix OB.
b) Please provide the promissory note for the debenture issued October 2, 2023 for
$200,000,000, explain whether the rate was 5.00% or 5.25%, and update the evidence as
required.
c) If any debt instruments have been issued since the preparation of the pre-filed evidence
for the current proceeding, please update the relevant evidence (including Appendix OA
and Appendix OB), and provide a copy of the relevant promissory note(s).
d) For each promissory note shown on Appendix OB with rates greater than the current
deemed long-term debt rate of 4.58%. please provide the following:
i. The start date of the debt.
ii. The deemed long-term debt rate in place at the time the debt was issued
iii. The need for the debt and rationale supporting taking the debt at the rate offered
e) Please provide rationale supporting the need for the forecasted debt issues shown in
Appendix OB, including any specific capital project(s) that the debt funding is for.
f) Please confirm that to determine the final revenue requirement for 2025 and the
subsequent years (i.e., 2026-2029), Toronto Hydro intends to use a long-term rate of
3.95%, or a different rate as updated through interrogatories. If this is not the case, please
explain.
```

**Query used for retrieval (locations stripped)**

```
Toronto Hydro stated that is had an all-in coupon rate of 4.93% on Toronto Hydro Corporation’s
(THC) 30-year issuance on August 28, 2023. However, OEB staff could not find this bond listed in
Toronto Hydro’s Appendix OB Debt Instruments for the rate year 2025.
In Appendix OB, Toronto Hydro indicated that on October 2, 2023, it had issued a debenture for
$200,000,000 with a rate of 5.25%, however, no promissory note was filed in Toronto Hydro’s
evidence in . Also, “Table 5: Forecasted Long-Term Debt Issues” on of
shows a forecasted rate of 5.00% and not 5.25% for the debt issued in October 2023.
The deemed long-term debt rate of 4.58% for electricity distributors was issued by the OEB on
October 31, 2023.
Toronto Hydro has calculated a long-term debt rate of 3.95% in Appendix OB for the 2025 rate
year. A long-term debt rate of 3.95% is also reflected in Toronto Hydro’s Excel revenue
requirement workforms for the rate years 2025 through 2029.
a) Please reconcile the debt that Toronto Hydro stated was issued on August 28, 2023 with
the debt issuances shown in Appendix OB.
b) Please provide the promissory note for the debenture issued October 2, 2023 for
$200,000,000, explain whether the rate was 5.00% or 5.25%, and update the evidence as
required.
c) If any debt instruments have been issued since the preparation of the pre-filed evidence
for the current proceeding, please update the relevant evidence (including Appendix OA
and Appendix OB), and provide a copy of the relevant pro
```

**Response**

```
The all-in coupon rate of 4.93% for 30-year THC debt issuance as at August 28, 2023 was an
indicative rate mentioned in the context of comparing credits spreads and absolute all-in-yields
between 2022 and 2023. There was no actual issuance of THC debt on August 28, 2023.

The promissory note issuances mentioned in Table 5 were forecasted long-term debt issuances.
There was no THC promissory note issuance on October 2, 2023. Toronto Hydro issued $200M
promissory note at an all-in coupon rate of 5.18% on October 12, 2023. Toronto Hydro has updated
Appendix OA-OB to reflect the same, which is attached as Appendix A to this interrogatory
response.

Please see the attached Appendix A and B to this response.

Toronto Hydro is assigned debt through promissory notes from its parent, Toronto Hydro
Corporation. These promissory notes are written on the same market terms as the parent debt
applicable to Toronto Hydro Corporation (plus an additional five basis points for an administration
fee). Toronto Hydro has the following promissory notes with rates greater than 4.58 percent:
Issuance -
Deemed long-term
debt rate at the time
Description
Amount ($)
Rate (%)
Start Date
of the debt
of issuance (%)
Actual/
Forecast
2022 Series 19 300,000,000
5.00%
13-Oct-22
3.49%
Actual
2023 Series 20 250,000,000
4.66%
14-Jun-23
4.88%
Actual
2023 Series 21 200,000,000
5.18%
12-Oct-23
4.88%
Actual
2024 Series 22 200,000,000
5.85%
01-Nov-24
4.58%
Forecast
2025 Series 23 300,000,000
5.45%
07-Jul-25
NA
Forecast
Toronto Hydro issues debt to fund its capital and operational requirements and to refinance its
maturing debt. For actual issuances, the rate reflects market conditions at the time of issuance.
The variance to the deemed long-term debt rate issued by OEB is mainly due to timing differences,
as OEB issued rates are calculated based on bond yields during the month of September for the
prior year.

To determine the final revenue requirement for the 2025-2029 rate period, the utility intends to use
a single long-term (“LT”) debt rate, which is currently 3.95% as supported by the evidence in Exhibit
6, Tab 1, Schedules 2-6. If during the course of the proceeding there are any updates or material
/C
changes to the evidence supporting the deemed LT rate during the course of the proceeding, Toronto
Hydro intends to update the rate accordingly and flow through the impact to the revenue
requirement impacts at the time of the Draft Rate Order process.
```

verdict: correct
label-for-query: yes

## 6. 1B-SEC-25  (doc `rds-867626`, pp. 803-803)

- gold (response) exhibits: **2B, 1B**
- reference-line exhibits: 1B
- PDF: http://localhost:3077/api/pdf/rds-867626#page=803

**Question (as filed)**

```
For each year between 2025-2029, please detail all productivity and efficiency initiatives that
Toronto Hydro plans to undertake. For each please provide a quantitative estimate of forecast
savings, and include the full methodology and assumptions used in the calculation.
```

**Query used for retrieval (locations stripped)**

```
For each year between 2025-2029, please detail all productivity and efficiency initiatives that
Toronto Hydro plans to undertake. For each please provide a quantitative estimate of forecast
savings, and include the full methodology and assumptions used in the calculation.
```

**Response**

```
Consistent with the expectations of the X-factor, the 2025-2029 Custom Scorecard includes an
Efficiency Achievements metric with a target to achieve approximately $6.9 million in sustained and
quantified efficiency benefits per year by the end of the rate period (i.e. 2029). Table 16 in the
referenced evidence details the types of investments that will enable Toronto Hydro to achieve the
$6.9 million target on this custom metric. Please refer to the utility’s response to 1B-SEC-20(f) for an
explanation of how these Efficiency Achievements will be tracked in the next rate period.
In the next rate period, the utility intends to continue to focus on process automation (e.g.
digitization, robotics and predictive analytics) to drive continuous improvement in efficiency and
productivity. A detailed list of specific initiatives will be determined as part of Toronto Hydro’s IT
Investment Planning process and Enterprise Technology Portfolio (ETP) framework as described in
Exhibit 2B, Section D8, pages 7-10. As initiatives are prioritized and approved for execution, expected
savings and benefits will be tracked and evaluated. Please see the evidence in Exhibit 1B, Tab 3,
Schedule 3 for a detailed list and explanation of over 30 productivity initiatives undertaken in the
current rate period, and the response to 1B-AMPCO-07 for more information about these initiatives.
```

verdict: correct
label-for-query: yes

## 7. 1B-CCC-27  (doc `rds-843530`, pp. 350-350)

- gold (response) exhibits: **1B**
- reference-line exhibits: 1B
- PDF: http://localhost:3077/api/pdf/rds-843530#page=350

**Question (as filed)**

```
Over the 2025-2029 rate period Toronto Hydro’s operations and capital investment needs are
growing by approximately 37.5% due to a number of distinct and interrelated drivers. Please
attribute a percentage to each of those drivers set out in the evidence. For example, how much of
the increases are related to inflationary pressures? How much s related to the aging and
deterioration of Toronto Hydro’s asset base?
```

**Query used for retrieval (locations stripped)**

```
Over the 2025-2029 rate period Toronto Hydro’s operations and capital investment needs are
growing by approximately 37.5% due to a number of distinct and interrelated drivers. Please
attribute a percentage to each of those drivers set out in the evidence. For example, how much of
the increases are related to inflationary pressures? How much s related to the aging and
deterioration of Toronto Hydro’s asset base?
```

**Response**

```
As noted, the drivers identified on page 7 of Exhibit 1B, Tab 2, Schedule 1 are “interrelated”, and
thus cannot be broken down as requested. At the reference noted, each driver is accompanied by a
footnote directing the reader to the evidence where detailed information, including cost breakdowns
as appropriate, about each driver can be found.
```

verdict: correct
label-for-query: yes

## 8. 4-STAFF-308  (doc `rds-851962`, pp. 47-52)

- gold (response) exhibits: **4**
- reference-line exhibits: 4
- PDF: http://localhost:3077/api/pdf/rds-851962#page=47

**Question (as filed)**

```
In reference 1 Toronto Hydro states it “needs to expand its workforce by approximately 214
resources starting in 2024 through 2029 to meet the imperatives and objectives of its 2025-2029
investment plan”.
Reference 3 is the Appendix 2-K submitted as part of the draft rate order in Toronto Hydro’s last
CIR application. It contains the forecast information for 2020. OEB staff have compiled the
information both versions of Appendix 2-K in the table below.

a) Please review and either verify or correct the information in the preamble.
b) Please confirm that and explain why, as shown in the preamble, almost half of the 214
hires required for the 2024-2029 period would occur in 2024.
c) Toronto states the non-management staff numbers decreased from the 2020 plan to 2021
actual largely due to impacts of the COVID-19 pandemic. Please confirm that non-
management numbers at the end of 2024 are forecast to be below the plan numbers for
2020.
d) Please explain the requirement for a 48% increase in management employees from 2020
plan to 2024 forecast.
e) Please explain the reason for the non-management staff to management staff ratio has
decreased from the 2020 plan to the 2024 bridge year and through the 2025-2029 forecast
period.
f) How does Toronto Hydro intend to execute its significantly larger capital plan for the
forecast period, compared to the historic period, with the proposed increase of non-
management staff during the forecast period over 2020 levels?
g) Please outline any projects THESL has, that Toronto Hydro is aware of, that will result in
increased services from Toronto Hydro, such as LED conversion of streetlights.
h) What would be the impact be to the 2 management positions and approximately 100 non-
management positions to be hired during the forecast period if there were reductions to
capital budget for 2025-2029 of 10, 20 or 30%?
```

**Query used for retrieval (locations stripped)**

```
In reference 1 Toronto Hydro states it “needs to expand its workforce by approximately 214
resources starting in 2024 through 2029 to meet the imperatives and objectives of its 2025-2029
investment plan”.
Reference 3 is the submitted as part of the draft rate order in Toronto Hydro’s last
CIR application. It contains the forecast information for 2020. OEB staff have compiled the
information both versions of in the table below.
a) Please review and either verify or correct the information in the preamble.
b) Please confirm that and explain why, as shown in the preamble, almost half of the 214
hires required for the 2024-2029 period would occur in 2024.
c) Toronto states the non-management staff numbers decreased from the 2020 plan to 2021
actual largely due to impacts of the COVID-19 pandemic. Please confirm that non-
management numbers at the end of 2024 are forecast to be below the plan numbers for
2020.
d) Please explain the requirement for a 48% increase in management employees from 2020
plan to 2024 forecast.
e) Please explain the reason for the non-management staff to management staff ratio has
decreased from the 2020 plan to the 2024 bridge year and through the 2025-2029 forecast
period.
f) How does Toronto Hydro intend to execute its significantly larger capital plan for the
forecast period, compared to the historic period, with the proposed increase of non-
management staff during the forecast period over 2020 levels?
g) Please outline any projects THESL has, that Tor
```

**Response**

```
Confirmed.

As stated in Exhibit 4, Tab 1, Schedule 1 at pages 22-23:
As Toronto Hydro prepares to enter its next rate period, staffing levels are forecasted to
grow by 25 percent over the 2024 through 2029 period. Due to the necessity of long lead
time investments in human capital (see below), this growth is higher in the beginning years
[i.e 2024 and 2025] and more gradual over the rest of the period, focused on scaling teams
that require additional resources and expanded skills to plan, design and execute capital
and operations work programs.
Just as it takes years to build new transformer station or convert an area of the city served
by legacy infrastructure to modern standards, human capital investments require long lead
times, with the average employee undergoing two years training and development before
becoming a fully competent contributor due to the specialized nature of the skills and
experience required to work in this sector. For certain trades, it takes anywhere from four
and a half to six and a half years to train a new certified and skilled tradesperson, plus a
minimum additional one to two years to develop a new frontline leader post
apprenticeship.
Toronto Hydro often hires capable, but relatively inexperienced employees, with the
intention to develop them in-house through on-the-job training and mentoring by tenured
staff who can ensure effective knowledge and skill transfer to the next generation of
employees.
In summary, hiring must be initiated in 2024 in order to have sufficient lead-time to recruit, onboard,
train and develop employees into fully competent contributors capable of meeting customers’
demands and delivering the 2025-2029 Investment Plan and its performance objectives. Without this
hiring in 2024, Toronto Hydro may not have the staffing capacity and capabilities it needs in the outer
years of the period. Please see Exhibit 4, Tab 4, Schedule 3, Table 1 at Pages 12 – 13 which speak to
the workforce skill sets and capabilities required to support asset investment plans.

Confirmed, however it is important to contextualize and understand why non-management numbers
at the end of 2024 are below the plan numbers for 2020. In the last rate application when the plan
line for 2020 was established, Toronto Hydro forecasted certain retirement projections and
associated hiring plans to replenish the aging workforce. Specifically, Toronto Hydro projected the
retirement of 278 employees by the end of 2021.1 Due to changing employee preferences arising
out of the global COVID-19 pandemic, the actual retirements from 2018-2021 exceeded the
projection by approximately 100 employees (see IR 4-AMPCO-83 for details). To put this in context,
the utility experienced an increase of one-third more employees departing the organization earlier
than planned, at a time during which it was also very challenging to hire and onboard new entrants
due to (i) social distancing restrictions imposed by the pandemic and remote work considerations
```

verdict: correct
label-for-query: yes (the 'EB-2018-0165, Exhibit 4A' footnote is no longer counted)

## 9. 1B-STAFF-8  (doc `rds-843530`, pp. 16-18)

- gold (response) exhibits: **3, 1B, 2B**
- reference-line exhibits: 1B
- PDF: http://localhost:3077/api/pdf/rds-843530#page=16

**Question (as filed)**

```
In Reference 1, Toronto Hydro shows that Toronto Hydro’s customer count has been slowing and is
projected to average 0.3% annually in the last three years of the rate period. The same reference
shows a downward trend in normalized MVA that is forecast to continue.
In Reference 2, Toronto Hydro states that “Toronto Hydro distributes electricity to Canada’s largest
- and North America’s second fastest growing city.”
Reference 4 indicates the City of Toronto’s population growth rate will slow.

a) Please explain Toronto Hydro’s view of the importance of absolute increase in population
as compared to the growth rate of a population in the context of planning a distribution
system. Please confirm that in the context of Toronto Hydro’s distribution system planning,
absolute growth is a more important consideration than the rate of growth. If not, please
explain.
b) Please reconcile the apparent discrepancy between the statement that the City of
Toronto’s population is growing, in absolute terms, more than other cities with Toronto
Hydro’s forecasts showing slowing system load growth rates and the Ontario Ministry of
Finance’s projections that population growth is slowing for the City of Toronto.
```

**Query used for retrieval (locations stripped)**

```
In Reference 1, Toronto Hydro shows that Toronto Hydro’s customer count has been slowing and is
projected to average 0.3% annually in the last three years of the rate period. The same reference
shows a downward trend in normalized MVA that is forecast to continue.
In Reference 2, Toronto Hydro states that “Toronto Hydro distributes electricity to Canada’s largest
- and North America’s second fastest growing city.”
Reference 4 indicates the City of Toronto’s population growth rate will slow.
a) Please explain Toronto Hydro’s view of the importance of absolute increase in population
as compared to the growth rate of a population in the context of planning a distribution
system. Please confirm that in the context of Toronto Hydro’s distribution system planning,
absolute growth is a more important consideration than the rate of growth. If not, please
explain.
b) Please reconcile the apparent discrepancy between the statement that the City of
Toronto’s population is growing, in absolute terms, more than other cities with Toronto
Hydro’s forecasts showing slowing system load growth rates and the Ontario Ministry of
Finance’s projections that population growth is slowing for the City of Toronto.
```

**Response**

```
Reference 1 above relates to customer and load growth changes from 2018 to 2029 for the
purpose of establishing a customer and load growth forecast to determine revenue to be collected
through rates, as fully described in Exhibit 3.
Reference 2 above contextualizes the size and characteristics of Toronto Hydro’s system and
customer base. Similar information is relied upon in the productivity evidence at Exhibit 1B, Tab 3,
Schedule 3 at pages 2 to 4, wherein Toronto Hydro describes its unique characteristics as a dense
urban distributor and the resulting operational challenges that it must manage in connecting and
serving its customers and carrying out prudent and necessary work to keep the system safe and
reliable in accordance with good utility practice.
Neither of the above references relate to growth for the purposes of distribution system planning,
which is articulated in full in Exhibit 2B, and summarized in Section A of that Exhibit at page 10:
“The growth is concentrated in certain pockets, namely the downtown core and along the transit
corridors, and is oriented vertically with a continuing trend of high-rise developments. This has
resulted is a marked need for new housing, transit solutions, and infrastructure, all of which needs
to be serviced by Toronto Hydro in the years to come.”
As outlined throughout the evidence in Exhibit 2B, distribution system planning is complex and
relies on a long list of varied inputs and planning considerations. There is no single metric of growth
relied upon to inform system planning.

Based on the response in part (a) above, Toronto Hydro submits there is no discrepancy, as
absolute growth and growth rates are referenced for different purposes in different contexts.
Both Reference 3 and Reference 4 are based on Statistics Canada data released in January 2023.
Reference 3 looks at growth over the preceding 12-month period and concludes that Toronto’s
population grew by 138,240 people, which is second only to Dallas-Fort Worth-Arlington in the cities
compared. Reference 4, on the other hand, is prospective and looks at population projections from
2022-2046. Reference 4 notes that Toronto’s population is projected to rise from 3.03 million in 2022
to 4.20 million in 2046, which is the largest population gain among the census divisions, but that the
rate growth of 37.7 percent is slightly slower than the provincial rate of growth of 43.6 percent.
```

verdict: correct
label-for-query: yes

## 10. 1B-STAFF-52  (doc `rds-843530`, pp. 143-147)

- gold (response) exhibits: **1B, 2B**
- reference-line exhibits: 1B
- PDF: http://localhost:3077/api/pdf/rds-843530#page=143

**Question (as filed)**

```
With Reference 1, Toronto Hydro shows the proposed 2025-2029 custom scorecard with 12
measures and targets.

a) Please reproduce Reference 1 with the following information:
i.
A column which indicates the total revenue requirement during the rate term of all
identified key programs associated with the delivery of the result, as detailed
throughout Reference 1.
ii.
A column which indicates the dollar value of the PIM at proposed weight and total
PIM envelope of $65M as proposed.
iii.
A column which indicates the calculated value of customer benefits realized in the
2025-2029 period (as identified in Table 21, p. 57, or elsewhere if applicable).
iv.
A column which indicates the ratio of iii) to ii) for each proposed PIM
b) Please Discuss:
i.
The proportion and significance of the PIM and its weighting within the PIM
framework, relative to the proportion and significance of identified key programs,
as provided in part i) above, in the context of Toronto Hydro’s overall spending
plan. Please evaluate how well the scope and value of its proposed PIMs
correspond with the scope and value of Toronto Hydro’s key spending and
investment areas within its plan.
ii.
The rationale and basis for the proportions of costs and benefits calculated in iv)
above, including variations in the observed ranges.
iii.
For any value where iii) is less than or equal to i), please explain Toronto Hydro’s
rationale for the particular PIM proposed, including its weight.
```

**Query used for retrieval (locations stripped)**

```
With Reference 1, Toronto Hydro shows the proposed 2025-2029 custom scorecard with 12
measures and targets.
a) Please reproduce Reference 1 with the following information:
i.
A column which indicates the total revenue requirement during the rate term of all
identified key programs associated with the delivery of the result, as detailed
throughout Reference 1.
ii.
A column which indicates the dollar value of the PIM at proposed weight and total
PIM envelope of $65M as proposed.
iii.
A column which indicates the calculated value of customer benefits realized in the
2025-2029 period (as identified in Table 21, p. 57, or elsewhere if applicable).
iv.
A column which indicates the ratio of iii) to ii) for each proposed PIM
b) Please Discuss:
i.
The proportion and significance of the PIM and its weighting within the PIM
framework, relative to the proportion and significance of identified key programs,
as provided in part i) above, in the context of Toronto Hydro’s overall spending
plan. Please evaluate how well the scope and value of its proposed PIMs
correspond with the scope and value of Toronto Hydro’s key spending and
investment areas within its plan.
ii.
The rationale and basis for the proportions of costs and benefits calculated in iv)
above, including variations in the observed ranges.
iii.
For any value where iii) is less than or equal to i), please explain Toronto Hydro’s
rationale for the particular PIM proposed, including its weight.
```

**Response**

```
Please see attached a table which lists each of the 12 scorecard metrics and targets, alongside a
column which assign a proportion of the proposed $65 million incentive to each metric, and a
column which assigns a proportion of quantifiable benefits realized over 2025 to 2029, as
presented in Exhibit 1B, Tab 3, Schedule 1.
Toronto Hydro cannot assign portions of its total revenue requirement to each metric on the
custom scorecard as there is not a one to one relationship between expenditures in these
programs and achieving specific performance metrics. Multiple programs contribute to multiple
performance objectives and it is not possible to attribute specific costs to specific measures and
targets. Toronto Hydro also notes that the request appears to infer that the capital and operational
programs detailed in this application are proposed on the basis and justification of target
achievement and associated economic benefits for customers. This is not the case. The capital and
OM&A program budgets proposed stand on their own merits, on the basis of the detailed evidence
submitted in Exhibits 2B and 4 describing the processes, needs, inputs, and other factors relied on
to conclude that the proposed 2025 to 2029 investment plan is the appropriate plan to meet the
needs of Toronto Hydro’s system and customers. The performance incentive is a complimentary
proposal to improve the balance of risk between the utility and ratepayers in responsiveness to the
OEB’s feedback in the last rate application.

Please see a) above with respect to the comparison of program costs and PIM incentives and
benefits. With respect to the PIM incentive relative to quantified benefits, the benefits received by
customers outweigh the cost of the PIM incentive in all scenarios, with the lifetime benefits
significantly outweighing the size of the PIM. This analysis does not take into account numerous
measures and targets (e.g. Customer Satisfaction, Customer Escalations, TRIF, Security
Enhancements, Grid Automation Readiness, ISO Certification) which although cannot reliably
quantified nonetheless provide long-term value to customers.
Page 1 of 2
Quantified Benefits
Ratio: Incentive vs.
Performance
Weight
Measures
Five-Year
Target
Incentive
Quantified Benefits
(2025-2029)
(Lifetime)
2025-29 Benefits
Ratio: Incentive vs.
Lifetime Benefits
15%
$9.8
$32.5
$605.2
3.33
62.02
Outage Duration: System Average Interruption
Duration Index (SAIDI) excluding Major Event
Days (MEDs), Loss of Supply (LoS) and
Scheduled Outages
46.2
minutes
(five-year
average)
System
Reliability &
$6.5
$6.5 - 21.6
$182.5 - 413.4
1.00 - 3.32
28.05 - 63.55
Resilience
10%
Outage Frequency: System Average
Interruption Frequency Index (SAIFI) -
Defective Equipment
0.38 – 0.45
(five-year
average)
5%
100% by
2029
$3.3
n/a
n/a
n/a
n/a
System Security Enhancements: Deliver
initiatives that enhance Toronto Hydro’s
physical and cyber security posture against the
NIST framework
10%
$6.5
$31.7 - 142.6
$31.7 - 142.6
4.87 -
```

verdict: correct
label-for-query: yes

## 11. 1B-STAFF-63  (doc `rds-843530`, pp. 178-179)

- gold (response) exhibits: **4**
- reference-line exhibits: 1B
- PDF: http://localhost:3077/api/pdf/rds-843530#page=178

**Question (as filed)**

```
Toronto Hydro states that increase in costs occurred in 2019 and 2020 due to switching from bi-
monthly billing to monthly billing.

Provide detailed explanation of increase in Billing O&M cost from 2018 to 2022 of more than
double 2018 customer billing costs.
Explain how productivity and economies of scale was not achieved with the adjustment of billing
period?
```

**Query used for retrieval (locations stripped)**

```
Toronto Hydro states that increase in costs occurred in 2019 and 2020 due to switching from bi-
monthly billing to monthly billing.
Provide detailed explanation of increase in Billing O&M cost from 2018 to 2022 of more than
double 2018 customer billing costs.
Explain how productivity and economies of scale was not achieved with the adjustment of billing
period?
```

**Response**

```
The Billing O&M costs provided in Table 10 do not provide a consistent representation of Toronto
Hydro’s unit cost per customer over the 2018-2022 period. The key contributing factors are: 1) the
introduction of monthly billing costs into the calculation; and 2) enhanced mapping precision
between the Ontario Energy Board USoA accounts 5315 and 5320 following the utility’s conversion
from the its legacy accounting system, Ellipse, to its current accounting system, SAP, in 2019.
As shown in Table 1, when USoA accounts 5315 and 5320 are combined from 2018 to 2022,
Toronto Hydro’s costs are accurately represented, including the impact of monthly billing starting
in 2020. Other variances are explained throughout Exhibit 4, Tab 2, Schedule 14.
Table 1: Combined USoA Accounts – 2018 to 2022
Accounts ($ million)
2018
Actual
2019
Actual
2020
Actual
2021
Actual
2022
Actual
Combined USoA accounts 5315 and 5320
23.3
22.2
26.4
25.1
28.5
As shown above, costs are relatively flat during the period of 2018 to 2022, when normalized for the
inclusion of $4.8 million in incremental costs for the conversion from bi-monthly billing to monthly
billing in 2020. A detailed discussion of the impact on costs related to the mandatory transition to
monthly billing can be found in Toronto Hydro’s 2020-2024 CIR rate application.1
The vast majority of costs associated with billing customers monthly are not subject to economies
of scale benefits. For example, postage, paper and printing, and payment processing costs, which
combined make up 64% of the incremental operational costs, are directly related to the number of
bills sent.
To minimize the incremental labour costs, Toronto Hydro undertook a number of initiatives,
including automation, process improvements, outsourcing and campaigns to drive ebill adoption.
An example was the replacement of "gatekeeper systems" which gather and transmit data from
meters to Toronto Hydro's billing system, which resulted in more timely and accurate data being
gathered automatically and reduced the labour (and associated costs) required to manually collect
and estimate hard to read meters. Along with the higher transactional volumes, labour economies
of scale were further improved through these initiatives, such that the FTE per 100,000 bills issued
reduced from approximately 4.5 FTEs in 2015 to 3.0 FTEs in 2020.
1 EB-2018-0165, Exhibit 9, Tab 1, Schedule 1, Page 20 to 31
```

verdict: correct
label-for-query: yes (gold is now Exhibit 4; the previous rate case's Exhibit 9 is no longer counted)

## 12. 1A-CCC-2  (doc `rds-845747`, pp. 212-215)

- gold (response) exhibits: **4, 1B, 3, 2A, 2B**
- reference-line exhibits: 1A
- PDF: http://localhost:3077/api/pdf/rds-845747#page=212

**Question (as filed)**

```
a) Please provide a complete list of all external consultants/lawyers Toronto engaged to assist it in
the development of the Application and pre-filed evidence;
b) For each engagement please provide the nature of the work and the retainer and terms of
reference;
c) Please provide the budgeted cost for the work for each engagement and the costs incurred to
date. Please indicate how the costs are to be recovered;
Please explain, in detail, how Toronto Hydro determined which areas of the Application should be
reviewed and validated by external experts;
1 Toronto Hydro notes that the cost noted here is only for the preparation of the report. For details on the
model development and implementation costs, please see Exhibit 2B-Staff-156.
Did Toronto Hydro develop an overall budget for this external work. If so, please indicate what
that budget was and how it was developed. If not, why not?
Please indicate whether each piece of work was subject to an RFP process. In those cases where
there was no RFP please explain why.
Did Toronto Hydro retain any external consultants and lawyers to undertake work related to the
Application that has not been included with the Application and pre-filed evidence?
```

**Query used for retrieval (locations stripped)**

```
a) Please provide a complete list of all external consultants/lawyers Toronto engaged to assist it in
the development of the Application and pre-filed evidence;
b) For each engagement please provide the nature of the work and the retainer and terms of
reference;
c) Please provide the budgeted cost for the work for each engagement and the costs incurred to
date. Please indicate how the costs are to be recovered;
Please explain, in detail, how Toronto Hydro determined which areas of the Application should be
reviewed and validated by external experts;
1 Toronto Hydro notes that the cost noted here is only for the preparation of the report. For details on the
model development and implementation costs, please see -Staff-156.
Did Toronto Hydro develop an overall budget for this external work. If so, please indicate what
that budget was and how it was developed. If not, why not?
Please indicate whether each piece of work was subject to an RFP process. In those cases where
there was no RFP please explain why.
Did Toronto Hydro retain any external consultants and lawyers to undertake work related to the
Application that has not been included with the Application and pre-filed evidence?
```

**Response**

```
The table below includes a list of all the consultants Toronto Hydro engaged to prepare expert
evidence for this rate application, the costs incurred to date (as of year-end 2023), and notes whether
the expert was engaged pursuant to an RFP. The total expected costs of the consultants depends on
the work required by these third parties to answer interrogatories, and the extent to which the OEB
and intervenors seek to have these third parties attend the hearing and be involved with other
procedural steps in this application. With the exception of certain studies undertaken in the normal
course of business, the cost of this work is managed through the consulting budget in Appendix 2-M
and is to be recovered through the Regulatory Affairs segment of the Public, Legal and Regulatory
Affairs program at Exhibit 4, Tab 1, Schedule 18. The budgeted costs for legal expenses are also set
out in Appendix 2-M. Please refer to 1B-SEC-11 for retainers for external service providers engaged
to prepare expert evidence.
Expert
Nature of Work /Evidence
Evidence Reference
RFP
Actual Costs
Reference
Customer Engagement
Incurred to
Date (2023)
Innovative
Research Group
Study
Exhibit 1B, Tab 5,
Schedule 1, App A
Yes
$760,661
Total Cost and Reliability
Benchmarking
Exhibit 1B, Tab 3,
Schedule 3, App A
Yes
Clearspring
Energy Advisors
$588,536
Load Forecast EV & DER
Integration
Exhibit 3, Tab 1,
Schedule 1, Appendix J
Yes
UMS Group Inc.
Unit Cost Benchmarking
Exhibit 1B, Tab 3,
Schedule 3, App C
No
$276,300
Scott Madden
Associates
Rate Framework Review
Exhibit 1B, Tab 2,
Schedule 1, Appendix A
Yes
$97,780
(USD)
Guidehouse
Lead/Lag Study
Exhibit 2A, Tab 3,
Schedule 2
No
$92,000
Concentric
Advisors
Financial Useful Lives
Exhibit 2A, Tab 2,
Schedule 1, Appendix D
Yes
$225,857
Exhibit 2B, Section D4,
EA Technology
Asset Condition
Assessment (ACA) Review
Appendix C
No
$53,500
(USD)
Element Energy
Future Energy Scenarios
Exhibit 2B, Section D4,
App B
Yes
$125,0001
IT Cost & Maturity
Exhibit 2B, Section D8,
Gartner
Consulting
Benchmarking
App A
No
$137,500
Stantec
Climate Change
Exhibit 2B, Section D2,
Vulnerability
App A
Yes
$29,374
Exhibit 4, Tab 4, Schedule
Mercer Canada
Compensation
Benchmarking
5
Yes
$79,999.75

Toronto Hydro used experience and professional judgment to determine which areas of the
application would benefit from review and/or validation from external consultants. Factors
included: guidance provided by the OEB in the RRF, the Handbook for Utility Rate Applications and
the Filing Requirements; what may be helpful to the OEB in understanding and assessing Toronto
Hydro’s application; and precedent from prior proceedings. In addition, some studies were
undertaken in the normal course of business and not for rate application business such as the
Climate Change Vulnerability Assessment.

The current budget for this work is included in the updated Appendix 2-M (found at Appendix A to
the response to Interrogatory 4-SEC-110). Please note that not all of the third-
```

verdict: wrong (a footnote from the response table, '1 Toronto Hydro notes that the cost noted here...', sits in the question field; the parts themselves are complete)
label-for-query: yes (exhibits are cited as where each consultant's evidence is filed; borderline)

## 13. 3-STAFF-278  (doc `rds-843536`, pp. 11-13)

- gold (response) exhibits: **2B**
- reference-line exhibits: -
- PDF: http://localhost:3077/api/pdf/rds-843536#page=11

**Question (as filed)**

```
Toronto Hydro used dummy variables RECLASS1, RECLASS2, and RECLASS3. OEB staff understands
that these variables would be intended to capture the impact of reclassification in the GS < 50 kW
and GS 50 - 999 kW rate classes.
The RECLASS variables start in June 2020, and are used one at a time, in sequence, until the end of
the forecast period.
The residential customer connection forecast relied on population as the only external variable
with a trend that varies over time. The same variable was used in the GS < 50 kW rate class. The GS
50-999 kW rate class used a measure of employment instead.

a) Please confirm OEB staff’s understanding of the purpose of these variables or explain.
b) Is Toronto Hydro able to count the number of customers reclassified?
i. If so, please provide the number of customers reclassified in/out each month.
ii. If so, why weren’t known values used as a manual adjustment?
c) What steps has Toronto Hydro taken to prevent trends or other causes of connection
change from being captured in the RECLASS variables?
d) Please explain the rationale for use of the population variable in the residential and GS <
50 kW rate class, and employment in the GS 50 - 999 kW rate class. Were different
variables attempted?
e) To what extent were customer connections impacted by the COVID-19 pandemic?
i. How is this reflected in the customer connection forecast?
```

**Query used for retrieval (locations stripped)**

```
Toronto Hydro used dummy variables RECLASS1, RECLASS2, and RECLASS3. OEB staff understands
that these variables would be intended to capture the impact of reclassification in the GS < 50 kW
and GS 50 - 999 kW rate classes.
The RECLASS variables start in June 2020, and are used one at a time, in sequence, until the end of
the forecast period.
The residential customer connection forecast relied on population as the only external variable
with a trend that varies over time. The same variable was used in the GS < 50 kW rate class. The GS
50-999 kW rate class used a measure of employment instead.
a) Please confirm OEB staff’s understanding of the purpose of these variables or explain.
b) Is Toronto Hydro able to count the number of customers reclassified?
i. If so, please provide the number of customers reclassified in/out each month.
ii. If so, why weren’t known values used as a manual adjustment?
c) What steps has Toronto Hydro taken to prevent trends or other causes of connection
change from being captured in the RECLASS variables?
d) Please explain the rationale for use of the population variable in the residential and GS <
50 kW rate class, and employment in the GS 50 - 999 kW rate class. Were different
variables attempted?
e) To what extent were customer connections impacted by the COVID-19 pandemic?
i. How is this reflected in the customer connection forecast?
```

**Response**

```
Toronto Hydro confirms OEB’s staff’s understanding of the variables.

Toronto Hydro is able to count the number of customers reclassified on an annual basis, as per
Customer Care processes.
Please refer to Table 1 below for the annual number of customers reclassified between 2020 and
2022 for the GS<50kW and GS 50-999 kW rate classes.
Table 1: Annual number of customers reclassified for GS<50kW and GS 50-999 kW rate classes
Year
GS<50 kW
GS 50-999 kW
2020
106
-206
2021
270
-294
2022
197
-198
i)
Toronto Hydro anticipates further reclassification in the future, and believes that
RECLASS indicator variable is the appropriate methodology to be used for GS<50 kW
and GS 50-999 kW rate classes for the following reasons: it creates a balance of good
model fit, appropriate causation and yield coefficient values that make practical and
statistical sense as well as provide good predictive value.

Toronto Hydro established RECLASS variables based on the historical timing of customer
reclassification, ensuring the suitability of explanatory variables in the model and minimizing the
influence of other factors being captured, as confirmed by the good fit.

Toronto Hydro tested several external variables to capture demographic and economic conditions,
create a balance of good model fit, and result in coefficient values that make practical and
statistical sense. The population and employment variables confirmed the best modeling results for
their respective rate classes.

As set out in Exhibit 2B, Section E5.1 Customer Connections, during the COVID-19 pandemic
Toronto Hydro’s historical trajectory of capital spend was maintained. This was also observed in
other data indicators such as the number of new connections, and feeder requests.
```

verdict: correct
label-for-query: yes

## 14. 4-STAFF-309  (doc `rds-851962`, pp. 53-57)

- gold (response) exhibits: **2B, 4, 1B**
- reference-line exhibits: 4
- PDF: http://localhost:3077/api/pdf/rds-851962#page=53

**Question (as filed)**

```
Toronto Hydro has proposed an increase to its workforce plan, particularly in the area of System
Planning, in part to support work related to the energy transition and electrification of its system,
including its grid modernization plan, flexibility services, including integration of DERs and Non-
Wires solutions.

a) Please provide a table that shows the staffing levels in the system planning group during
the current rate period and the proposed 2025-2029 rate period.
b) Please indicate the number of staff proposed to be dedicated to work related to the energy
transition, the roles of the staff, a general description of their responsibilities, and salary
levels for the roles.
c) Please discuss the need and identify the specific projects/tasks that the proposed new staff
related to the energy transition and electrification (including grid modernization, DER
integration and non-wires solutions) will be assigned over the 2025-2029 period.
d) Has Toronto Hydro retained staffing with the required knowledge to deliver local and/or
Province-Wide CDM programs (currently offered through the IESO) should policy change
and local distribution companies be provided a path for greater program activity? If yes,
please discuss how these staff have been incorporated into other business functions, and
the ease with which they could manage additional responsibilities should they be required.
```

**Query used for retrieval (locations stripped)**

```
Toronto Hydro has proposed an increase to its workforce plan, particularly in the area of System
Planning, in part to support work related to the energy transition and electrification of its system,
including its grid modernization plan, flexibility services, including integration of DERs and Non-
Wires solutions.
a) Please provide a table that shows the staffing levels in the system planning group during
the current rate period and the proposed 2025-2029 rate period.
b) Please indicate the number of staff proposed to be dedicated to work related to the energy
transition, the roles of the staff, a general description of their responsibilities, and salary
levels for the roles.
c) Please discuss the need and identify the specific projects/tasks that the proposed new staff
related to the energy transition and electrification (including grid modernization, DER
integration and non-wires solutions) will be assigned over the 2025-2029 period.
d) Has Toronto Hydro retained staffing with the required knowledge to deliver local and/or
Province-Wide CDM programs (currently offered through the IESO) should policy change
and local distribution companies be provided a path for greater program activity? If yes,
please discuss how these staff have been incorporated into other business functions, and
the ease with which they could manage additional responsibilities should they be required.
```

**Response**

```
Table 1 below describes FTE staffing levels in the system planning group during the current rate
period and the proposed 2025-2029 rate period.
Table 1: FTE Staffing Levels in System Planning – 2020 to 2029
Segment Name
Actuals
Bridge
Forecast
2020
2021
2022
2023
2024
2025
2026
2027
2028
2029
System Planning
62
70
81
82
98
105
115
119
120
120

Toronto Hydro cannot provide the requested breakdown as the System Planning program does not
have a dedicated pool of resources allocated to energy transition. Over the next rate period, Toronto
Hydro’s system investment needs are growing and the challenges of system planning are becoming
more complex due to energy transition and other interrelated drivers described in the evidence at
Exhibit 2B. To deal effectively with these System Planning needs and challenges, Toronto Hydro must
increase resourcing in this area by 38 FTEs over the next rate term, for the reasons that follow.
Increasing Capital Work Volume: By far the most significant driver of this increase is the general
increase in capital work across the Growth, Sustainment, and Modernization programs (detailed
throughout Exhibit 2B, Section E), driven in part, but not exclusively by, the energy transition. With
an 47% increase in capital investment across the various system investment programs, there is a
correlating need to scale-up the available pool of engineering and analyst resources who are
responsible for studying the system, identifying projects, developing those projects into detailed
scopes of work, and advising on changes to the projects as they move through design and execution.
Toronto Hydro will also need greater support in the Records Management area to keep pace with
the higher volume of changes in asset information related to the completion of incremental capital
work. While none of these incremental positions will be “dedicated” to the energy transition, they
will all be contributing to ensuring that Toronto Hydro is able to facilitate customers’ increased and
evolving use of electricity. They will be part of an expanded pool of resources dealing with a volume
of work that is greater in part because of the demands of electrification, decarbonization, and
Distributed Energy Resource (“DER”) proliferation. Figure 1 in Exhibit 4, Tab 2, Schedule 9 shows the
expected increase in the value of scopes of work and demand program expenditures (primarily
customer connections and generation connections) in 2025-2029.
Grid Modernization and Continuous Improvement in Asset Management: The other driver of this
increase is the need to adequately support the modernization efforts detailed throughout Toronto
Hydro’s DSP. Toronto Hydro has outlined various plans to accelerate its efforts to apply technology,
innovation, and best practices to enhance the value derived from its assets (“asset performance”)
and its Asset Management System (“asset management capabilities”). These efforts are broadly
outlined in Exhibit 2B, Section D1.2.1.1, and further 
```

verdict: correct
label-for-query: yes

## 15. 2B-STAFF-161  (doc `rds-846609`, pp. 175-175)

- gold (response) exhibits: **2B**
- reference-line exhibits: 2B
- PDF: http://localhost:3077/api/pdf/rds-846609#page=175

**Question (as filed)**

```
Toronto Hydro writes that it is “adding more sensors, relays and monitoring technology at specific
nodes across the distribution grid, including customer meters. These assets will provide additional
data collection points across the grid, which Toronto Hydro will leverage to improve overall
situational awareness (“grid transparency”), facilitate quicker fault location, and gain access to
important insights at the edge of the grid.”

a) Please provide several representative examples where Toronto Hydro is proposing to put
these sensors and relays and explain why they are being proposed for these locations
relative to the rest of Toronto Hydro’s territory.
```

**Query used for retrieval (locations stripped)**

```
Toronto Hydro writes that it is “adding more sensors, relays and monitoring technology at specific
nodes across the distribution grid, including customer meters. These assets will provide additional
data collection points across the grid, which Toronto Hydro will leverage to improve overall
situational awareness (“grid transparency”), facilitate quicker fault location, and gain access to
important insights at the edge of the grid.”
a) Please provide several representative examples where Toronto Hydro is proposing to put
these sensors and relays and explain why they are being proposed for these locations
relative to the rest of Toronto Hydro’s territory.
```

**Response**

```
To clarify, the reference to “specific nodes” is intended to convey the fact that there are various
locations within the design of the distribution system (as opposed to the geography) where certain
sensors and technologies can provide value. Some examples include:
•
AMI 2.0 meters, which provide observability and control at the customer-level;
•
Network Condition Monitoring and Control technologies, which provide observability and
control on Toronto Hydro’s network system; and
•
Stations Digital Relays, which provide observability and control at the stations level.
For a comprehensive overview of how these technologies support Toronto Hydro’s Grid
Modernization Strategy, and how the utility is pacing and prioritizing deployment, please refer to
Exhibit 2B, Section D5.2.1 and Sections E5.4, E6.6, and E7.3.
```

verdict: correct
label-for-query: yes

## 16. 1B-PP-12  (doc `rds-867626`, pp. 54-54)

- gold (response) exhibits: **1B**
- reference-line exhibits: -
- PDF: http://localhost:3077/api/pdf/rds-867626#page=54

**Question (as filed)**

```
“the majority of Key Account customers surveyed have goals to reduce their net
GHG emissions to zero, and expect Toronto Hydro to support them in meeting their
climate objectives by ensuring that the system has capacity for growth and by
providing them advisory services to support their decarbonization-through-
electrification journey” [Investment Plan Section 3.1] Please provide any references
that support this observation (e.g. THESL key account interactions, survey
questions, etc.).
```

**Query used for retrieval (locations stripped)**

```
“the majority of Key Account customers surveyed have goals to reduce their net
GHG emissions to zero, and expect Toronto Hydro to support them in meeting their
climate objectives by ensuring that the system has capacity for growth and by
providing them advisory services to support their decarbonization-through-
electrification journey” [Investment Plan ] Please provide any references
that support this observation (e.g. THESL key account interactions, survey
questions, etc.).
```

**Response**

```
Customers were asked “Does your organization have a carbon reduction program in place? Page 31
of Exhibit 1B, Tab 5, Schedule 1, Appendix A, - Customer Engagement Report, Appendix.06 – Key
Accounts shows that a majority (64%) of Toronto Hydro’s key account customers had “net zero”
targets or carbon reduction initiatives in place at the time of the Phase I Needs and Preferences
Survey consisting of:
•
38% reporting carbon reduction targets currently in place, and
•
26% reporting “net zero” targets.
Additionally, page 28 of Appendix.01 – Qualitative Research documents that many key account
participants interviewed in Phase I “shared their hopes that Toronto Hydro would increase their
support in helping them transition to lower or non-emitting carbon energy sources, building out
more distributed energy resources (including battery storage), and enabling grid modernization,
such as microgrids technologies”.
```

verdict: correct
label-for-query: yes

## 17. 1B-CCC-37  (doc `rds-843530`, pp. 361-365)

- gold (response) exhibits: **4, 2B**
- reference-line exhibits: 1B
- PDF: http://localhost:3077/api/pdf/rds-843530#page=361

**Question (as filed)**

```
Toronto Hydro is proposing a Demand-Related Variance Account (DRVA) to record the demand
driven revenue requirement impacts arising from variances in actual versus forecast capital and
operational expenditures for certain demand-based programs and the revenue impacts arising
from variances in forecast versus actual billing determinants over the rate period. The Council
is interested in understanding the scope of the DRVA;

a) For each year 2020-2024 please provide the forecast and actual expenditures for the
following capital and operating programs: Customer Connections, Customer Operations,
Stations Expansion, Load Demand, Non-Wires Solutions, Generation Protection Monitoring
and Control and Externally-initiated Plant Relocations and Expansions. Also, please provide
the forecast and actual revenue requirement that would have been dealt with through the
DRVA Expenditure sub-account had one been in place for that period;
b) For each year 2025-2029 please provide the proposed revenue requirement for each of the
programs listed in a). In effect, what is the proposed revenue requirement that will be the
subject of the DRVA Expenditure Variance sub-account?
c) For the period 2020-2024 please provide the forecast and actual revenue that would
have been dealt with through the DRVA Variance sub-account had one been in place for
that period
7 Rounding variances may exist
d) For each year 2025-2029 please provide the forecast revenue that will be the subject of the
DRVA Revenue Variance sub-account.
```

**Query used for retrieval (locations stripped)**

```
Toronto Hydro is proposing a Demand-Related Variance Account (DRVA) to record the demand
driven revenue requirement impacts arising from variances in actual versus forecast capital and
operational expenditures for certain demand-based programs and the revenue impacts arising
from variances in forecast versus actual billing determinants over the rate period. The Council
is interested in understanding the scope of the DRVA;
a) For each year 2020-2024 please provide the forecast and actual expenditures for the
following capital and operating programs: Customer Connections, Customer Operations,
Stations Expansion, Load Demand, Non-Wires Solutions, Generation Protection Monitoring
and Control and Externally-initiated Plant Relocations and Expansions. Also, please provide
the forecast and actual revenue requirement that would have been dealt with through the
DRVA Expenditure sub-account had one been in place for that period;
b) For each year 2025-2029 please provide the proposed revenue requirement for each of the
programs listed in a). In effect, what is the proposed revenue requirement that will be the
subject of the DRVA Expenditure Variance sub-account?
c) For the period 2020-2024 please provide the forecast and actual revenue that would
have been dealt with through the DRVA Variance sub-account had one been in place for
that period
7 Rounding variances may exist
d) For each year 2025-2029 please provide the forecast revenue that will be the subject of the
DRVA Revenue Variance
```

**Response**

```
Please see below Table 1 for Actuals/Bridge Capital Expenditures and Table 2 for Actuals/Bridge
Operating Expenditures. In responding to this interrogatory Toronto Hydro has only included
OM&A segments that would have been dealt with through the DRVA expenditure sub-account had
one been in place for that period.
Table 1: Actuals/Bridge Capital Expenditures that would have been subject to the DRVA sub-
account (in $ millions)
Actuals
Bridge
Programs
2020
2021
2022
2023
2024
Customer Connections
35.6
92.4
76.1
86.8
78.2
Stations Expansion
18.2
50.3
47.5
10.4
16.1
Load Demand
24.0
29.7
30.8
26.7
23.2
Non-Wires Solutions1
1.0
0.5
0.1
0.0
0.6
Generation Protection Monitoring & Control1
0.8
0.8
0.1
0.2
7.8
Externally Initiated Plant Relocations &
Expansions
8.7
9.3
12.9
16.0
13.0
Table 2: Actuals/Bridge Operating Expenditures that would have been subject to the DRVA sub-
account (in $ millions)
OM&A Segments2
Actuals
Bridge
2020
2021
2022
2023
2024
Customer Connections, Exhibit 4, Tab 2, Schedule
8, Section 5
3.7
1.6
1.6
3.1
3.6
Key Accounts, Exhibit 4, Tab 2, Schedule 8,
Section 6
-
0.5
0.8
0.8
1.2
Flexibility Services, Exhibit 2B, Section E7.2
0.4
0.2
0.2
0.8
0.8
Please see Table 3 for approved Capital Expenditures and Table 4 for approved Operating
Expenditures that would have been dealt with through the DRVA expenditure sub-account had one
been in place for that period.
Table 3: Approved Capital Expenditures that would have been subject to DRVA sub-account (in $
millions)
Approved
Programs
2020
2021
2022
2023
2024
Customer Connections
40.1
40.9
41.7
42.6
43.4
1 94% of the Renewable Enabling portions of these investments will be provincially funded and not included
in the DRVA
2 Only includes segments associated with the DRVA
Approved
Programs
2020
2021
2022
2023
2024
Stations Expansion
19.5
40.0
49.3
12.5
15.2
Load Demand
11.3
11.4
18.5
22.6
23.6
Non-Wires Solutions3
1.0
3.7
3.8
1.0
1.0
Generation Protection Monitoring & Control3
3.7
2.3
2.4
2.5
2.7
Externally Initiated Plant Relocations &
Expansions
11.4
20.8
4.6
4.7
4.5
As noted in Toronto Hydro’s response to interrogatory 4-SEC-89(a), the total OM&A cost approved
by the OEB for 2020 was $266.7 million, which was lower than the 2020 test year OM&A funding
requested by Toronto Hydro. 4 The OEB approved OM&A on an envelope basis and therefore,
Toronto Hydro cannot provide a breakdown by the specific programs or segments such as Customer
connections. However, in order to provide a directional view of the segments that would have been
dealt through the DRVA expenditure sub-account had one been in place for that period, Toronto
Hydro has used its 2020 test5 costs for Customer Connections, Key Accounts and Flexibility Services
and have escalated it by the OEB approved Custom Price Cap Index (“CPCI”) formula6 for 2021-2024
using OEB’s prescribed rates.
Table 4: Approved* Operating Expenditures that would have been subject to the DRVA sub-
account (in $ millions)
Approved*
OM&A Segments
2020
2021
2022
20
```

verdict: wrong (exhibits appear as table row labels for segments, not as where the requested figures are; a response footnote, '7 Rounding variances may exist', sits in the question field)
label-for-query: no (same reason)

## 18. 1B-STAFF-19  (doc `rds-843530`, pp. 50-53)

- gold (response) exhibits: **1B**
- reference-line exhibits: 1B
- PDF: http://localhost:3077/api/pdf/rds-843530#page=50

**Question (as filed)**

```
Page 2 of Reference 1, Toronto Hydro states:
“the Company’s proposed changes to the Rate Framework are generally consistent with
how other electric utilities have responded to developments in the energy industry. [italics
added]”
On page 3:
“Given these developments in the energy industry, many regulatory jurisdictions have
implemented changes to ratemaking frameworks and practices. These changes are
designed to incorporate expanded objectives and priorities, such as clean energy goals,
affordability, reliability, emission reduction, and utility financial integrity.”

a) Please confirm the following statements. If Toronto Hydro disagrees with any or all of
these statements, please explain why.
i.
Toronto Hydro already operates under an approach to custom incentive rate-
setting that it has dubbed CIR 1.0.
1. This ratemaking system includes a price cap index formula with a C factor
that effectively replaces capital revenue growth based primarily on
inflation and productivity indexing with capital revenue growth based
primarily on a cost forecast.
2. The inflation measure in this formula includes a relevant input price index:
the average weekly earnings on Ontario workers.
3. An asymmetrical Capital-Related Revenue Requirement Variance Account
returns any and all capital-related revenue requirement savings to
customers.
4. There is also a two-way variance account for miscellaneous externally-
driven costs.
ii.
Toronto Hydro’s new CIR proposal entails the following changes from its old
proposal.
1.A revenue growth factor (“RGF”) would effectively replace OM&A as well
as capital revenue growth based primarily on inflation and productivity
indexing with growth that is based primarily on cost forecasts.
2. A revenue cap index would replace the price cap index, and a demand
revenue variance account (“DRVA”) would effectively establish weather-
normalized revenue decoupling.
3. The DRVA would also establish two-way variance account treatment for a
wide range of demand-sensitive costs.
4. The Capital-Related Revenue Requirement Variance Account would be
discontinued.
5.There would, additionally be an Innovation Fund, a Getting Ontario
Connected Act Variance Account, and PIM tied to customer service quality
and various policy goals.
b) Does Toronto Hydro mean that each of these changes is individually consistent with
industry trends or instead that many of these changes are consistent with industry trends?
c) Is Toronto Hydro stating that ratemaking in North America
```

**Query used for retrieval (locations stripped)**

```
of Reference 1, Toronto Hydro states:
“the Company’s proposed changes to the Rate Framework are generally consistent with
how other electric utilities have responded to developments in the energy industry. [italics
added]”
On :
“Given these developments in the energy industry, many regulatory jurisdictions have
implemented changes to ratemaking frameworks and practices. These changes are
designed to incorporate expanded objectives and priorities, such as clean energy goals,
affordability, reliability, emission reduction, and utility financial integrity.”
a) Please confirm the following statements. If Toronto Hydro disagrees with any or all of
these statements, please explain why.
i.
Toronto Hydro already operates under an approach to custom incentive rate-
setting that it has dubbed CIR 1.0.
1. This ratemaking system includes a price cap index formula with a C factor
that effectively replaces capital revenue growth based primarily on
inflation and productivity indexing with capital revenue growth based
primarily on a cost forecast.
2. The inflation measure in this formula includes a relevant input price index:
the average weekly earnings on Ontario workers.
3. An asymmetrical Capital-Related Revenue Requirement Variance Account
returns any and all capital-related revenue requirement savings to
customers.
4. There is also a two-way variance account for miscellaneous externally-
driven costs.
ii.
Toronto Hydro’s new CIR proposal entails the following changes from its old
propos
```

**Response**

```
i.
Confirm.
1. Partially confirm. The C factor is subject to inflation and productivity factors.
2. Partially confirmed. The inflation factor includes a labour and non-labour component.
3. Confirm.
4. Confirm.
ii.
1) Partially confirm. The RGF factor is still subject to inflation and productivity factors.
2) Partially confirm. DRVA trues up billing determinants on a weather normalized basis.
3) Confirm.
4) Confirm.
5) Confirm.

ScottMadden did not evaluate industry trends. Instead, ScottMadden evaluated Toronto Hydro’s
proposed custom IR plan for its relative consistency with other electric utility ratemaking
frameworks and practices that support a clean energy transition. Please refer to the response to
1B-EP-23, part (a).

ScottMadden did not evaluate industry trends. Instead, ScottMadden evaluated Toronto Hydro’s
proposed custom IR plan for its relative consistency with other electric utility ratemaking
frameworks and practices that support a clean energy transition. Please refer to the response to
1B-EP-23, part (a).

ScottMadden did not evaluate trends in variance account treatment. Please refer to the response
to 1B-EP-23, part (a).

Please refer to Figure 1 in Exhibit 1B-2-1 Appendix A, (Review of Rate Framework), pp. 5-6.
```

verdict: correct
label-for-query: yes

## 19. 1B-STAFF-16  (doc `rds-843530`, pp. 37-41)

- gold (response) exhibits: **2B, 4, 1B**
- reference-line exhibits: -
- PDF: http://localhost:3077/api/pdf/rds-843530#page=37

**Question (as filed)**

```
At page 26, Reference 1 states:
“Custom IR is not a multi-year cost of service; explicit financial incentives for continuous
improvement and cost control targets must be included in the application.”

a) Please describe Toronto Hydro’s proposals for continuous improvement within the rate
term, with specific reference to its preference for targets to be established on a five-year
basis rather than annually, as noted at page 31 of Reference 2.
b) What commitments, if any, does Toronto Hydro make to customers about improvements in
cost and service performance to be achieved within the five-year term?
```

**Query used for retrieval (locations stripped)**

```
At , Reference 1 states:
“Custom IR is not a multi-year cost of service; explicit financial incentives for continuous
improvement and cost control targets must be included in the application.”
a) Please describe Toronto Hydro’s proposals for continuous improvement within the rate
term, with specific reference to its preference for targets to be established on a five-year
basis rather than annually, as noted at of Reference 2.
b) What commitments, if any, does Toronto Hydro make to customers about improvements in
cost and service performance to be achieved within the five-year term?
```

**Response**

```
Toronto Hydro’s proposals for continuous improvements within the rate term are found both
within and beyond the 2025-2029 Custom Scorecard and related targets that underpin the
Performance Incentive Mechanism (“PIM”).
Within the 2025-2029 Custom Scorecard and related PIM, Toronto Hydro has put forward various
new performance measures and objectives that reflect the utility’s ongoing commitment to
continuous improvement. More specifically:
•
reducing the duration of unplanned outages that customers experience;
•
enhancing physical and cyber security threat detection and mitigation in accordance with
NIST standards;
•
advancing grid automation readiness for the horseshoe area of the grid by increasing
remote operability of the distribution system and laying the foundation for self-healing;
•
holding itself accountable for delivering demonstrative efficiency achievements
commensurate with the expectations of the empirical stretch-factor proposed as part of
the rate framework;
•
tracking and reporting post-transactional customer satisfaction performance with respect
to customer inquiries (phone and email), Key Accounts engagements, customer
connections, and customer communications re planned outages and construction projects.
•
tracking, reporting and resolving customer escalations in a timely manner.
•
achieving and maintaining certification with international best practices (ISO) in various key
management systems.
•
reducing the company’s GHG emissions in a paced and prudent manner
•
expanding the scope of non-wires solutions by procuring 30MW of flexible capacity to
address system capacity constraints.
The proposal for targets to be established on a five-year basis rather than annually reflect the
necessary and practical considerations of: (i) operational complexity and uncertainty that the utility
must manage in the normal course of business serving the needs of customers in a large, dense,
urban environment; (ii) the multi-year nature of the work that utility needs to perform in order to
achieve the target objectives reflects an integrated five-year plan (not five one-year plans); and (iii)
the need to preserve operational flexibility within this integrated five-year plan to execute work
programs effectively.
Outside of the 2025-2029 Custom Scorecard, Toronto Hydro’s commitment to continuous
improvement is detailed throughout the evidence. Notable examples include:
•
Continuous improvement of the Asset management system, including:
o Continue to improve the maturity of Toronto Hydro’s asset risk management
framework through the full implementation of the Condition Based Risk
Management (“CBRM”) methodology and fully embedding the Engineering Asset
Investment Planning (“EAIP”) solution within asset management processes,
including a custom value framework to enable portfolio optimization.
o Develop Toronto Hydro’s Asset Information Strategy to improve the quality of
asset data and related data sources to support improved analytics & asset
manageme
```

verdict: correct
label-for-query: yes

## 20. 2B-AMPCO-28  (doc `rds-843534`, pp. 27-29)

- gold (response) exhibits: **2B, 4**
- reference-line exhibits: 2B
- PDF: http://localhost:3077/api/pdf/rds-843534#page=27

**Question (as filed)**

```
AMPCO seeks to further understand how Toronto Hydro prioritizes projects comparatively at the
project and portfolio level. Is this a manual or automated process? How did Toronto Hydro
optimize its project portfolio?
```

**Query used for retrieval (locations stripped)**

```
AMPCO seeks to further understand how Toronto Hydro prioritizes projects comparatively at the
project and portfolio level. Is this a manual or automated process? How did Toronto Hydro
optimize its project portfolio?
```

**Response**

```
Details on Toronto Hydro’s project prioritization are discussed in Exhibit 2B, Section D1.2.1.4, page
23, and Exhibit 2B, Section D1.2.3, page 25. This process is currently manual and is managed as part
of Toronto Hydro’s Program Management and Execution process, particularly the Execution Work
Program (“EWP”) as discussed in Exhibit 4, Tab 2, Schedule 9, Section 8.
The development of the EWP is iterative in nature and involves continuous coordination between
program managers and system planners to ensure alignment with strategic objectives. Planning
teams assign priority levels to their projects that are then considered along with factors such as
project labour requirements, schedules and resources to determine the prioritized mix of projects
to be executed in a given year. As part of the forecasting process high and medium priority projects
are assigned for execution ahead of low priority projects. The EWP forecasting process includes a
daily consolidation of inputs from all operations teams to provide visibility on the project selection
alignment to the portfolio targets and inclusion of all high priority projects. This consolidation is
reviewed throughout the EWP forecasting process with key stakeholders to adjust and align the
forecast selection to the portfolio targets as closely as possible while still considering program
execution constraints.
Toronto Hydro’s process for project prioritization is anticipated to evolve once its new EAIP
optimization tool has been embedded as part of its business planning process.
Note that Toronto Hydro’s 2025-2029 investment plan is not based on project details.
RESPONSES TO ASSOCIATION OF MAJOR POWER CONSUMERS IN ONTARIO
INTERROGATORIES
```

verdict: correct
label-for-query: yes
