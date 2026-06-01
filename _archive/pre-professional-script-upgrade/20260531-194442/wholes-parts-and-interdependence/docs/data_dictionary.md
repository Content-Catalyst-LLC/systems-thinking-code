# Data Dictionary

## synthetic_system_parts.csv

- `part_id`: unique identifier for each system part
- `part_name`: readable name
- `level`: nested system level
- `part_type`: institutional, technical, ecological, social, informational, or governance
- `criticality`: low, medium, or high
- `baseline_capacity`: synthetic 0-100 capacity score

## synthetic_dependency_edges.csv

- `source`: dependent or influencing part
- `target`: part that receives influence or dependency
- `dependency_type`: resource, information, authority, operational, ecological, or social
- `weight`: synthetic strength of dependency
- `delay`: short, medium, or long

## synthetic_part_whole_levels.csv

- `level_id`: level identifier
- `level_name`: readable name
- `parent_level`: broader nested level

## synthetic_scenarios.csv

- `scenario_id`: unique scenario identifier
- `scenario_name`: readable scenario name
- `shock_part`: part where disturbance begins
- `shock_size`: synthetic shock magnitude
- `redundancy_multiplier`: assumed redundancy condition
- `coordination_multiplier`: assumed coordination condition

## synthetic_indicators.csv

- `period`: model period
- `system_capacity`: synthetic whole-system capacity indicator
- `dependency_stress`: synthetic stress indicator
- `resilience_buffer`: synthetic resilience indicator
- `coordination_quality`: synthetic coordination indicator
- `local_performance`: synthetic local component indicator
- `whole_system_outcome`: synthetic whole-system outcome indicator
