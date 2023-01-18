// Run: `deno run --allow-read 2.ts`
import { readline } from 'https://deno.land/x/readline@v1.1.0/mod.ts';

type Outcome = 'loss' | 'draw' | 'win';
type EnemyMove = 'A' | 'B' | 'C';
type YourMove = 'X' | 'Y' | 'Z';

interface Matchup {
  enemy: EnemyMove;
  you: YourMove;
}

type OutcomeCondition = Record<EnemyMove, Record<YourMove, Outcome>>;

type OutcomeType = Record<EnemyMove, Record<Outcome, YourMove>>;

const TYPE_SCORE = {
  X: 1,
  Y: 2,
  Z: 3,
};

const OUTCOME_SCORE = {
  loss: 0,
  draw: 3,
  win: 6,
};

const OUTCOME_CONDITION: OutcomeCondition = {
  A: {
    X: 'draw',
    Y: 'win',
    Z: 'loss',
  },
  B: {
    X: 'loss',
    Y: 'draw',
    Z: 'win',
  },
  C: {
    X: 'win',
    Y: 'loss',
    Z: 'draw',
  },
};

const TYPE_OUTCOME: Record<YourMove, Outcome> = {
  X: 'loss',
  Y: 'draw',
  Z: 'win',
};

const OUTCOME_TYPE: OutcomeType = {
  A: {
    draw: 'X',
    win: 'Y',
    loss: 'Z',
  },
  B: {
    loss: 'X',
    draw: 'Y',
    win: 'Z',
  },
  C: {
    win: 'X',
    loss: 'Y',
    draw: 'Z',
  },
};

const matchScore = (move: YourMove, outcome: Outcome): number =>
  TYPE_SCORE[move] + OUTCOME_SCORE[outcome];

const matchOutcome = (enemyMove: EnemyMove, yourMove: YourMove): Outcome => {
  return OUTCOME_CONDITION[enemyMove][yourMove];
};

const matchMove = (enemyMove: EnemyMove, yourOutcome: Outcome): YourMove => {
  return OUTCOME_TYPE[enemyMove][yourOutcome];
};

const processMatches = (matches: Array<Matchup>): number[] => {
  let totalScoreA = 0;
  let totalScoreB = 0;

  matches.forEach((match: Matchup): void => {
    totalScoreA += matchScore(match.you, matchOutcome(match.enemy, match.you));
    totalScoreB += matchScore(
      matchMove(match.enemy, TYPE_OUTCOME[match.you]),
      TYPE_OUTCOME[match.you]
    );
  });

  return [totalScoreA, totalScoreB];
};

const parseInput = async (filename = './input.txt'): Promise<Matchup[]> => {
  const f = await Deno.open(filename);
  const matches: Array<Matchup> = [];

  for await (const rawLine of readline(f)) {
    const line = new TextDecoder().decode(rawLine);
    const splitLine = line.split(' ');

    matches.push({
      enemy: splitLine[0] as EnemyMove,
      you: splitLine[1] as YourMove,
    });
  }

  return matches;
};

const matches = await parseInput();
console.log('Total score A is ', processMatches(matches)[0]);
console.log('Total score B is ', processMatches(matches)[1]);
