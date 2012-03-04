/*
 * stl_stable_partition.cpp
 *
 *  Created on: 2011-5-29
 *      Author: xyf
 */
/*
 || Using the STL stable_partition algorithm
 || Takes any number of flags on the command line and
 || four filenames in order.
 */
#include <string>
#include <list>
#include <algorithm>
#include<iostream>

using namespace std;

void PrintIt(string& AString) {
	cout << AString << endl;
}

class IsAFlag {
public:
	bool operator ()(string& PossibleFlag) {
		return PossibleFlag.substr(0, 1) == "-";
	}
};

class IsAFileName {
public:
	bool operator ()(string& StringToCheck) {
		return !IsAFlag()(StringToCheck);
	}
};

class IsHelpFlag {
public:
	bool operator ()(string& PossibleHelpFlag) {
		return PossibleHelpFlag == "-h";
	}
};

int main(int argc,char* argv[]) {

	list<string> CmdLineParameters; // the command line parameters
	list<string>::iterator StartOfFiles; // start of filenames
	list<string> Flags; // list of flags
	list<string> FileNames; // list of filenames
	for (int i = 0; i < argc; ++i)
		CmdLineParameters.push_back(argv[i]);

	CmdLineParameters.pop_front(); // we don't want the program name
   // for_each(CmdLineParameters.begin(),CmdLineParameters.end(),PrintIt);

	// make sure we have the four mandatory file names
	// make sure we have the four mandatory file names
	int NumberOfFiles(0);
	NumberOfFiles=count_if(CmdLineParameters.begin(), CmdLineParameters.end(),IsAFileName());
	cout << "The " << (NumberOfFiles == 4 ? "correct " : "wrong ")
			<< "number (" << NumberOfFiles << ") of file names were specified"
			<< endl;

	// move any flags to the beginning
	StartOfFiles = stable_partition(CmdLineParameters.begin(),
			CmdLineParameters.end(), IsAFlag());
	//cout << endl;
	//for_each(StartOfFiles, CmdLineParameters.end(), PrintIt);

	cout << "Command line parameters after stable partition" << endl;
	for_each(CmdLineParameters.begin(), CmdLineParameters.end(), PrintIt);

	// Splice any flags from the original CmdLineParameters list into Flags list.
	Flags.splice(Flags.begin(), CmdLineParameters, CmdLineParameters.begin(),
			StartOfFiles);

	if (!Flags.empty()) {
		cout << "Flags specified were:" << endl;
		for_each(Flags.begin(), Flags.end(), PrintIt);
	} else {
		cout << "No flags were specified" << endl;
	}

	// parameters list now contains only filenames. Splice them into FileNames list.
	FileNames.splice(FileNames.begin(), CmdLineParameters,
			CmdLineParameters.begin(), CmdLineParameters.end());

	if (!FileNames.empty()) {
		cout << "Files specified (in order) were:" << endl;
		for_each(FileNames.begin(), FileNames.end(), PrintIt);
	} else {
		cout << "No files were specified" << endl;
	}

	// check if the help flag was specified
	if (find_if(Flags.begin(), Flags.end(), IsHelpFlag()) != Flags.end()) {
		cout << "The help flag was specified" << endl;
	}

	if(CmdLineParameters.empty())
		cout <<"CmdLineParameters"<<endl;

	// open the files and do whatever you do

	return 0;
}

