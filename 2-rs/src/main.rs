use std::collections::HashMap;

fn matchup_score(otucome: i32, choice: char) {
  let scoreA = outcome_score.get(&outcome);
  let scoreB = choice_score.get(&choice);

  return scoreA + scoreB;
}

fn main() {
  let outcome_score = HashMap::from([
    ("WIN", 6),
    ("DRAW", 3),
    ("LOSS", 0),
  ]);

  let choice_score = HashMap::from([
    ('X', 1),
    ('Y', 2),
    ('Z', 3),
  ]);

  let matchups = HashMap::from([
      ('A', ['Y', 'Z']),
      ('B', ['Z', 'X']),
      ('C', ['X', 'Y']),
  ]);

  let closure_matchups = | outcome: i32, choice: char | + 

  println!("{}", closure_matchups("WIN", 'X'));
}