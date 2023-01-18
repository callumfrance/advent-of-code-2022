import { readline } from 'https://deno.land/x/readline@v1.1.0/mod.ts';

const TOTAL_ROUNDS = 20;

type Operation = '*' | '/' | '+' | '-';

interface TestConditions {
  operation: Operation;
  mutatorValue: number | 'old';
  testThreshold: number;
}

interface Monkey {
  items: Array<number>;
  testConditions: TestConditions;
  passMonkey: number;
  failMonkey: number;
  inspectionCount: number;
}

const worryAttrition = (worry: number): number => Math.floor(worry / 3);

const monkeyBusiness = (monkeyA: Monkey, monkeyB: Monkey): number =>
  monkeyA.inspectionCount * monkeyB.inspectionCount;

const performTest = (
  testConditions: TestConditions,
  value: number
): boolean => {
  const fixedOperand: number =
    testConditions.mutatorValue === 'old' ? value : testConditions.mutatorValue;

  switch (testConditions.operation) {
    case '*':
      return (value * fixedOperand) % testConditions.testThreshold === 0;
    case '/':
      return (value / fixedOperand) % testConditions.testThreshold === 0;
    case '+':
      return (value + fixedOperand) % testConditions.testThreshold === 0;
    case '-':
      return (value - fixedOperand) % testConditions.testThreshold === 0;
    default:
      throw Error('This should be unreachable');
  }
};

const computeRound = (currentMonkeys: Monkey[]): Monkey[] => {
  const monkeyRound: Monkey[] = [];

  currentMonkeys.forEach((currentMonkey: Monkey, index: number): void => {});

  return monkeyRound;
};

const calculateMonkeyBusiness = (monkeys: Monkey[]): number => {
  let highestInspectionMonkeys: Monkey[] = [];

  monkeys.forEach((currentMonkey: Monkey): void => {
    if (
      highestInspectionMonkeys[1].inspectionCount <
      currentMonkey.inspectionCount
    ) {
      highestInspectionMonkeys = [highestInspectionMonkeys[1], currentMonkey];
    } else if (
      highestInspectionMonkeys[0].inspectionCount <
      currentMonkey.inspectionCount
    ) {
      highestInspectionMonkeys = [currentMonkey, highestInspectionMonkeys[1]];
    }
  });

  return monkeyBusiness(
    highestInspectionMonkeys[0],
    highestInspectionMonkeys[1]
  );
};

const computeAllRounds = (
  monkeys: Monkey[],
  totalRounds: number = TOTAL_ROUNDS
): number => {
  for (let i = 0; i < totalRounds; i++) {
    monkeys = computeRound(monkeys);
  }

  return calculateMonkeyBusiness(monkeys);
};

const parseInput = async (filename = './input.txt'): Promise<Monkey[]> => {
  const f = await Deno.open(filename);
  const monkeys: Array<Monkey> = [];

  let workingMonkey: Partial<Monkey> = {
    items: [],
    testConditions: {
      mutatorValue: 0,
      operation: '+',
      testThreshold: 0,
    },
    passMonkey: 0,
    failMonkey: 0,
    inspectionCount: 0,
  };

  let workingTestConditions: TestConditions = {
    mutatorValue: 0,
    operation: '+',
    testThreshold: 0,
  };

  for await (const rawLine of readline(f)) {
    const line = new TextDecoder().decode(rawLine);

    if (line) {
      const splitLine = line.split(' ');

      switch (splitLine[0]) {
        case 'Monkey':
          break;
        case 'Starting':
          workingMonkey.items = splitLine
            .slice(2)
            .map((item) => parseInt(item));
          break;
        case 'Operation:':
          if (splitLine.slice(-1)[0] === 'old') {
            workingTestConditions.mutatorValue = 'old';
          } else {
            workingTestConditions.mutatorValue = parseInt(
              splitLine.slice(-1)[0]
            );
          }
          workingTestConditions.operation = splitLine.slice(
            -2,
            -1
          )[0] as Operation;
          break;
        case 'Test:':
          workingTestConditions.testThreshold = parseInt(
            splitLine.slice(-1)[0]
          );
          workingMonkey.testConditions = workingTestConditions;
          break;
        case 'If':
          switch (splitLine[1]) {
            case 'true:':
              workingMonkey.passMonkey = parseInt(splitLine.slice(-1)[0]);
              break;
            case 'false:':
              workingMonkey.failMonkey = parseInt(splitLine.slice(-1)[0]);
              break;
          }
      }
    } else {
      monkeys.push(workingMonkey as Monkey);
    }
  }

  return monkeys;
};

console.log(computeAllRounds(await parseInput()));
