package main

import (
	"fmt"
	"log"
	"regexp"
	"sort"
	"strconv"
	"time"

	"github.com/johnshiver/advent_of_code/2018/utils"
)

var timeStampAndTextRe *regexp.Regexp
var guardRe *regexp.Regexp

var timeStampFormat = "2006-01-02 15:04"

func init() {
	timeStampAndTextRe = regexp.MustCompile(`\[(\d*-\d*-\d* \d*:\d*)\] ([\w\s#]*)`)
	guardRe = regexp.MustCompile(`Guard #(\d*) [\w\s#]*`)
}

type recordLine struct {
	TimeStamp     time.Time
	Text          string
	GuardID       int
	Status        string
	minutesAwake  int
	minutesAsleep int
}

func (rl *recordLine) isGuard() bool {
	return rl.minutesAsleep == 0 && rl.minutesAwake == 0
}

const ASLEEP = "asleep"
const AWAKE = "awake"

func createRecord(rawRecord string) (*recordLine, error) {
	recordElements := timeStampAndTextRe.FindStringSubmatch(rawRecord)
	timeStamp, err := time.Parse(timeStampFormat, recordElements[1])
	if err != nil {
		return &recordLine{}, err
	}
	text := recordElements[2]
	return &recordLine{TimeStamp: timeStamp, Text: text}, nil
}

func attachGuardIDs(records []*recordLine) []*recordLine {
	// records must be sorted by TimeStamp
	sort.Slice(records, func(i, j int) bool {
		return records[i].TimeStamp.Before(records[j].TimeStamp)
	})
	var currID int
	var minutesAwake int
	var minutesAsleep int
	var previous *recordLine
	for _, r := range records {

		var status string
		switch r.Text {
		case "falls asleep":
			status = ASLEEP
		case "wakes up":
			status = AWAKE
		default:
			status = AWAKE
		}

		guardElements := guardRe.FindStringSubmatch(r.Text)
		// we have reached a new guard, reset ID
		if len(guardElements) > 0 {
			rawID := guardElements[1]
			newID, err := strconv.Atoi(rawID)
			if err != nil {
				log.Fatal(err)
			}
			currID = newID
			minutesAsleep = 0
			minutesAwake = 0
		} else {
			if previous.Status == ASLEEP {
				minutesAsleep += int(r.TimeStamp.Sub(previous.TimeStamp).Minutes())
				minutesAwake = 0
			} else {
				minutesAwake += int(r.TimeStamp.Sub(previous.TimeStamp).Minutes())
				minutesAsleep = 0
			}
		}
		r.minutesAwake = minutesAwake
		r.minutesAsleep = minutesAsleep
		r.GuardID = currID
		r.Status = status
		previous = r
	}
	return records
}

func createMinutesGrid(guardRecords []*recordLine) []int {
	minutesGrid := make([]int, 61)
	var previous *recordLine
	for _, r := range guardRecords {
		if r.Status == AWAKE && previous != nil && !r.isGuard() {
			for x := previous.TimeStamp; x.Before(r.TimeStamp); x = x.Add(time.Minute) {
				minutesGrid[x.Minute()]++
			}
		}
		previous = r
	}
	return minutesGrid
}

func strategyOne(guardRecords map[int][]*recordLine) (int, int) {
	var largestGuardID int
	var mostMinutes int
	for guardID, records := range guardRecords {
		minutesSlept := 0
		for _, r := range records {
			minutesSlept += r.minutesAsleep
		}
		if minutesSlept > mostMinutes {
			largestGuardID = guardID
			mostMinutes = minutesSlept
		}
	}
	minutesGrid := make([]int, 61)
	var previous *recordLine
	for _, r := range guardRecords[largestGuardID] {
		if r.Status == AWAKE && previous != nil && !r.isGuard() {
			for x := previous.TimeStamp; x.Before(r.TimeStamp); x = x.Add(time.Minute) {
				minutesGrid[x.Minute()]++
			}
		}
		previous = r
	}
	var largestVal int
	var largestIndex int
	for i, v := range minutesGrid {
		if v > largestVal {
			largestVal = v
			largestIndex = i
		}
	}
	return largestGuardID, largestIndex
}

func strategyTwo(guardRecords map[int][]*recordLine) (int, int) {
	var guardMinuteGrid = make(map[int][]int)
	for guardID, records := range guardRecords {
		guardMinuteGrid[guardID] = createMinutesGrid(records)
	}

	var largestGuardID int
	var mostFrequent int
	var largestIndex int
	for guardID, minuteGrid := range guardMinuteGrid {
		for i, v := range minuteGrid {
			if v > mostFrequent {
				mostFrequent = v
				largestIndex = i
				largestGuardID = guardID
			}
		}
	}

	return largestGuardID, largestIndex
}

func createGuardRecordsMap(records []*recordLine) map[int][]*recordLine {
	// records must be sorted by TimeStamp
	sort.Slice(records, func(i, j int) bool {
		return records[i].TimeStamp.Before(records[j].TimeStamp)
	})
	guardRecordsMap := make(map[int][]*recordLine)
	for _, r := range records {
		guardRecordsMap[r.GuardID] = append(guardRecordsMap[r.GuardID], r)
	}
	return guardRecordsMap
}

func main() {
	rawRecords, err := utils.ReadFileofStrings("input.txt")
	if err != nil {
		log.Fatal(err)
	}
	var records []*recordLine
	for _, r := range rawRecords {
		newRecord, err := createRecord(r)
		if err != nil {
			log.Fatal(err)
		}
		records = append(records, newRecord)
	}
	attachGuardIDs(records)
	guardRecordsMap := createGuardRecordsMap(records)
	guardID, minute := strategyOne(guardRecordsMap)
	fmt.Println(guardID, minute)
	fmt.Println(guardID * minute)
	guardID, minute = strategyTwo(guardRecordsMap)
	fmt.Println(guardID, minute)
	fmt.Println(guardID * minute)
}
