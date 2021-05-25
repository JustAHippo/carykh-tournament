# carykh-tournament
A repo of possible scripts for CaryKH's Prisoners Dilemma tournament in which utilize weights in order to sway decision-making in many different ways

All of these scripts use fine decisionmaking based on the player's last move. While Drowzee and realisticDrowzee implement a bit of randomness, impulsiveDrowzee and immediateDrowzee make immediate decisions based only on past moves by the other player.

# Each file's use
Name  | Use
| :------------ |:---------------:|
Drowzee  | Starts off with copying the player's move. Slowly averages and randomizes based on it.
realisticDrowzee  | Starts off at total randomness and builds off from there based on player decisions.
immediateDrowzee | Starts off at 0.5. As rounds go, if the weight is higher than 0.5, it is immediately a cooperate and vice versa.
impulsiveDrowzee | Starts off at copying, and then follows as if it were immediateDrowzee
