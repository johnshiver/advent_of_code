package main

import (
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
	TimeStamp time.Time
	Text      string
	GuardID   int
}

func createRecord(rawRecord string) (recordLine, error) {
	recordElements := timeStampAndTextRe.FindStringSubmatch(rawRecord)
	timeStamp, err := time.Parse(timeStampFormat, recordElements[1])
	if err != nil {
		return recordLine{}, err
	}

	return recordLine{TimeStamp: timeStamp, Text: recordElements[2]}, nil

}

func attachGuardIDs(records []recordLine) []recordLine {
	// records must be sorted by TimeStamp
	sort.Slice(records, func(i, j int) bool {
		return records[i].TimeStamp.Before(records[j].TimeStamp)
	})
	currID := -1
	for _, r := range records {
		guardElements := guardRe.FindStringSubmatch(r.Text)
		if len(guardElements) > 0 {
			rawID := guardElements[1]
			currID, err := strconv.Atoi(rawID)
		}
	}
	return records
}

func main() {
	rawRecords, err := utils.ReadFileofStrings("input.txt")
	if err != nil {
		log.Fatal(err)
	}
	var records []recordLine
	for _, r := range rawRecords {
		newRecord, err := createRecord(r)
		if err != nil {
			log.Fatal(err)
		}
		records = append(records, newRecord)
	}
	attachGuardIDs(records)
}
