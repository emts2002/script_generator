from tkinter import filedialog

class Region:
    def __init__(self, city_list, unit_list, chance_list, region_n, no_of_men, exp_list, unit_n_list):
        self.cities = city_list
        self.units = unit_list
        self.chances = chance_list
        self.region_n = region_n
        self.no_of_men = no_of_men
        self.exp = exp_list
        self.unit_n = int(city_list[len(city_list) - 1])
        self.cities.pop(len(self.cities) - 1)
        self.unit_n_list = unit_n_list
    
    def printtofile1(self, file, n):
        print("\t\tif\tSettlementName " + self.cities[0], file = file)
        for i in range(1, len(self.cities)):
            print("\t\t\t|| SettlementName " + self.cities[i], file = file)
        print("\t\t\tset_counter local_region_number" + str(n) + " " + str(self.region_n), file = file)
        print("\t\tend_if", file = file)
        
    def printtofile2(self, file, n):
        print("\t\tif\tI_CompareCounter region_id = " + str(self.region_n), file = file)
        print("\t\t\tdeclare_counter unit_n\n\t\t\tset_counter unit_n "+str(self.unit_n), file = file)
        print("\t\t\twhile_not\tI_CompareCounter unit_n <= 0", file = file)
        print("\t\t\t\tdeclare_counter chance_taken\n\t\t\t\tset_counter chance_taken 0", file = file)
        a = 1
        for i in range(len(self.units) - 1):
            print("\t\t\t\tif	RandomPercent <= " + str(self.chances[i]*100/a), file = file)
            print("\t\t\t\t\t&& I_CompareCounter unit_n >= "+str(self.unit_n_list[i]), file = file)
            print("\t\t\t\t\t&& I_CompareCounter chance_taken = 0\n\t\t\t\t\tset_counter chance_taken 1\n\t\t\t\t\tdeclare_counter exp_took\n\t\t\t\t\tset_counter exp_took 0", file = file)
            print("\t\t\t\t\tinc_counter unit_n -"+str(self.unit_n_list[i]), file = file)
            b = 1
            for j in range(9):
                if b != 0:
                    print("\t\t\t\t\tif	RandomPercent <= " + str(self.exp[i][j]*100/b), file = file)
                else:
                    print("\t\t\t\t\tif	RandomPercent < 0", file = file)
                print("\t\t\t\t\t\t&& I_CompareCounter exp_took = 0\n\t\t\t\t\t\tset_counter exp_took 1", file = file)
                print('\t\t\t\t\t\tconsole_command create_unit local_settlement "' + self.units[i] + '" 1 ' + str(j) + ' 0 0', file = file)
                print("\t\t\t\t\tend_if", file = file)
                b -= self.exp[i][j]
            print("\t\t\t\t\tif	I_CompareCounter exp_took = 0", file = file)
            print("\t\t\t\t\t\tset_counter exp_took 1", file = file)
            print('\t\t\t\t\t\tconsole_command create_unit local_settlement "' + self.units[i] + '" 1 9 0 0', file = file)
            print("\t\t\t\t\tend_if", file = file)
            a -= self.chances[i]
                
                
                
            print("\t\t\t\t\tconsole_command add_population local_settlement " + str(-self.no_of_men[len(self.units) - 1]), file = file)
            print("\t\t\t\tend_if", file = file)
            
        print("\t\t\t\tif	I_CompareCounter chance_taken = 0", file = file)
        print("\t\t\t\t\t&& I_CompareCounter unit_n >= "+str(self.unit_n_list[len(self.unit_n_list) - 1]), file = file)
        print("\t\t\t\t\tset_counter chance_taken 1\n\t\t\t\t\tdeclare_counter exp_took\n\t\t\t\t\tset_counter exp_took 0", file = file)
        print("\t\t\t\t\tinc_counter unit_n -"+str(self.unit_n_list[len(self.unit_n_list) - 1]), file = file)
        b = 1
        for j in range(9):
            if b != 0:
                print("\t\t\t\t\tif	RandomPercent <= " + str(self.exp[len(self.units) - 1][j]*100/b), file = file)
            else:
                print("\t\t\t\t\tif	RandomPercent < 0", file = file)
            print("\t\t\t\t\t\t&& I_CompareCounter exp_took = 0\n\t\t\t\t\t\tset_counter exp_took 1", file = file)
            print('\t\t\t\t\t\tconsole_command create_unit local_settlement "' + self.units[len(self.units) - 1] + '" 1 ' + str(j) + ' 0 0', file = file)
            print("\t\t\t\t\tend_if", file = file)
            b -= self.exp[len(self.units) - 1][j]
        print("\t\t\t\t\tif	I_CompareCounter exp_took = 0", file = file)
        print("\t\t\t\t\t\tset_counter exp_took 1", file = file)
        print('\t\t\t\t\t\tconsole_command create_unit local_settlement "' + self.units[len(self.units) - 1] + '" 1 9 0 0', file = file)
        print("\t\t\t\t\tend_if", file = file)
        print("\t\t\t\t\tconsole_command add_population local_settlement " + str(-self.no_of_men[len(self.units) - 1]), file = file)
        print("\t\t\t\tend_if", file = file)
        print("\t\t\tend_while", file = file)
        print("\t\tend_if", file = file)
   
def random_unit_from_unit(ilines, dummy_unit_list):
    nextlineindex = 0
    nextline = ilines[0]
    unit_name = nextline[5:]
    nextlineindex += 1
    nextline = ilines[nextlineindex]
    region_list = []
    region_n = 1
    while nextline.startswith("pool"):
        city_list = nextline.split(" ")
        city_list.pop(0)
        nextlineindex += 1
        nextline = ilines[nextlineindex]
        unit_list = []
        chance_list = []
        no_of_men = []
        exp_list = []
        unit_n_list = []
        while not (nextline.startswith("pool") or nextline.startswith("unit") or nextline == "end" or nextline == ""):
            new_unit = nextline.split(" ")
            unit_list.append(new_unit[0].replace('_', ' '))
            chance_list.append(float(new_unit[1]))
            no_of_men.append(int(new_unit[2]))
            exp = new_unit[3:]
            unit_n_list.append(exp[len(exp) - 1])
            exp.pop(len(exp) - 1)
            for i in range(len(exp)):
                exp[i] = float(exp[i])
            exp_list.append(exp)
            nextlineindex += 1
            nextline = ilines[nextlineindex]
        region_list.append(Region(city_list, unit_list, chance_list, region_n, no_of_men, exp_list, unit_n_list))
        region_n += 1
    dummy_unit_list.append((unit_name, region_list))
        
class UnitToRegenerate:
    def __init__(self, unit, faction_list, condition_list, chance, min_r, max_r, r_inc):
        self.unit = unit
        self.faction_list = faction_list
        self.building_list = condition_list[0]
        self.resource_list = condition_list[1]
        self.chance = chance
        self.min_r = min_r
        self.max_r = max_r
        self.r_inc = r_inc
        
    def printtofile(self, file):
        print("\tmonitor_event FactionTurnEnd TrueCondition", file = file)
        for faction in self.faction_list:
            print("\t\tif\tFactionType "+faction, file = file)
            print('\t\t\tfor_each\tsettlement in faction "'+faction+'"', file = file)
            if len(self.building_list) > 0:
                print("\t\t\t\tif\tSettlementBuildingExists >= "+self.building_list[0], file = file)
                for building in self.building_list[1:]:
                    print("\t\t\t\t\t&& SettlementBuildingExists >= "+building, file = file)
                for resource in self.resource_list:
                    print("\t\t\t\t\t&& HasResource >= "+resource, file = file)
            elif len(self.resource_list) > 0:
                print("\t\t\t\tif\tHasResource >= "+self.resource_list[0], file = file)
                for resource in self.resource_list[1:]:
                    print("\t\t\t\t\t&& HasResource >= "+resource, file = file)
            else:
                print("\t\t\t\tif\tRandomPercent > -1", file = file)
            print("\t\t\t\t\tfor_each\tunit in settlement", file = file)
            print("\t\t\t\t\t\tif\tUnitType "+self.unit, file = file)
            print("\t\t\t\t\t\t\t&& RandomPercent < "+str(self.chance)+"\n\t\t\t\t\t\t\tdeclare_counter random_chance\n\t\t\t\t\t\t\tset_counter random_chance 0", file = file)
            
            n = (self.max_r - self.min_r) / self.r_inc + 1
            
            print("\t\t\t\t\t\t\tif\tRandomPercent <= "+str(int(1/n*100)), file = file)
            print("\t\t\t\t\t\t\t\tset_counter random_chance 1", file = file)
            print('\t\t\t\t\t\t\t\tconsole_command add_soldiers local_settlement '+str(self.min_r)+' 80 "'+self.unit+'" 1 "soldier_count"', file = file)
            print("\t\t\t\t\t\t\tend_if", file = file)
            for i in range(self.min_r + self.r_inc, self.max_r + 1, self.r_inc):
                n -= 1
                print("\t\t\t\t\t\t\tif\tRandomPercent <= "+str(int(1/n*100)), file = file)
                print("\t\t\t\t\t\t\t\t&& I_CompareCounter random_chance = 0", file = file)
                print("\t\t\t\t\t\t\t\tset_counter random_chance 1", file = file)
                print('\t\t\t\t\t\t\t\tconsole_command add_soldiers local_settlement '+str(i)+' 80 "'+self.unit+'" 1 "soldier_count"', file = file)
                print("\t\t\t\t\t\t\tend_if", file = file)
            
            print("\t\t\t\t\t\tend_if", file = file)
            print("\t\t\t\t\tend_for", file = file)
            print("\t\t\t\tend_if", file = file)
            print("\t\t\tend_for", file = file)
            print("\t\tend_if", file = file)
        print("\tend_monitor", file = file)
        
def unit_regeneration(ilines, unit_regeneration_list):
    unit = ilines[0]
    faction_list = ilines[1].split(" ")
    faction_list.pop(0)
    building_list = ilines[2].split(" ")
    building_list.pop(0)
    resource_list = ilines[3].split(" ")
    resource_list.pop(0)
    condition_list = (building_list, resource_list)
    min_r = int(ilines[4][15:])
    max_r = int(ilines[5][15:])
    r_inc = int(ilines[6][15:])
    chance = int(ilines[7][7:])
    unit_regeneration_list.append(UnitToRegenerate(unit, faction_list, condition_list, chance, min_r, max_r, r_inc))
    
class UnitPoolLR:
    def __init__(self, pool, units, regions, start, maximum, regen_chance):
        self.units = units
        self.regions = regions
        self.start = start
        self.maximum = maximum
        self.regen_chance = regen_chance
        self.pool = pool
        
    def printtofile1(self, file):
        if self.regions[0] == "all":
            print("\tfor_each\tsettlement in world", file = file)
            print("\t\tdeclare_counter a\n\t\tset_counter a "+ self.start, file = file)
            print("\t\tstore_counter a settlement "+self.pool+"_pool", file = file)
            if int(self.start) > 0:
                print("\t\tadd_hidden_resource local "+self.pool+"_available", file = file)
            print("\tend_for", file = file)
        else:
            for region in self.regions:
                print("\tadd_hidden_resource "+region+" "+self.pool+"_recruitment", file = file)
                if int(self.start) > 0:
                    print("\tadd_hidden_resource "+region+" "+self.pool+"_available", file = file)
            print("\tfor_each\tsettlement in world\n\t\tif\tHasReesource "+self.pool+"_recruitment", file = file)
            print("\t\t\tdeclare_counter a\n\t\t\tset_counter a "+ self.start, file = file)
            print("\t\t\tstore_counter a settlement "+self.pool+"_pool", file = file)
            print("\t\tend_if\n\tend_for", file = file)
            
    def printtofile2(self, file):
        if self.regions[0] == "all":
            print("\tmonitor_Event\tNewTurnStart TrueCondition\n\t\tfor_each\tsettlement in world", file = file)
            print("\t\t\tdeclare_counter pool\n\t\t\tretrieve_counter "+self.pool+"_pool settlement pool", file = file)
            print("\t\t\tif\tI_CompareCounter pool < "+self.maximum, file = file)
            print("\t\t\t\t&& RandomPercent <= "+self.regen_chance, file = file)
            print("\t\t\t\tinc_counter pool 1\n\t\t\tend_if\n\t\t\tif\tI_CompareCounter pool > 0", file = file)
            print("\t\t\t\t&& not HasResource "+self.pool+"_available", file = file)
            print("\t\t\t\tadd_hidden_resource local "+self.pool+"_available\n\t\t\tend_if\n\t\tend_for\n\tend_monitor", file = file)
            
        else:
            print("\tmonitor_Event\tNewTurnStart TrueCondition\n\t\tfor_each\tsettlement in world", file = file)
            print("\t\t\tif\tHasResource "+self.pool+"_recruitment", file = file)
            print("\t\t\t\tdeclare_counter pool\n\t\t\t\tretrieve_counter "+self.pool+"_pool settlement pool", file = file)
            print("\t\t\t\tif\tI_CompareCounter pool < "+self.maximum, file = file)
            print("\t\t\t\t\t&& RandomPercent <= "+self.regen_chance, file = file)
            print("\t\t\t\t\tinc_counter pool 1\n\t\t\t\tend_if\n\t\t\t\tif\tI_CompareCounter pool > 0", file = file)
            print("\t\t\t\t\t&& not HasResource "+self.pool+"_available", file = file)
            print("\t\t\t\t\tadd_hidden_resource local "+self.pool+"_available\n\t\t\t\tend_if\n\t\t\tend_if\n\t\tend_for\n\tend_monitor", file = file)
        
        for unit in self.units:
            print("\tmonitor_event\tUnitTrained UnitType "+unit, file = file)
            print("\t\tdeclare_counter pool\n\t\tretrieve_counter "+self.pool+"_pool settlement pool", file = file)
            print('\t\tif\tI_CompareCounter pool = 0\n\t\t\tconsole_command destroy_unit local_settlement "'+unit+'" 1 "soldier_count"', file = file)
            print("\t\tend_if\n\t\tif\tI_CompareCounter pool > 0\n\t\t\tinc_counter pool -1", file = file)
            print("\t\t\tif\tI_CompareCounter pool < 1\n\t\t\t\tremove_hidden_resource local "+self.pool+"_available", file = file)
            print("\t\t\tend_if\n\t\t\tstore_counter pool settlement "+self.pool+"_pool\n\t\tend_if\n\tend_monitor", file = file)
        
    def printinstructions(self, file):
            print('\t"'+self.pool+'_available":\n\t{\n\t\t"subtype": "hidden",\n\t},', file = file)
            if not self.regions[0] == "all":
                print('\t"'+self.pool+'_recruitment":\n\t{\n\t\t"subtype": "hidden",\n\t},', file = file)
        
def limited_recruitment_unit_pool(ilines, limited_recruitment_unit_pool_list):
    pool = ilines[0].split(" ")[1]
    units = ilines[1].split(" ")
    units.pop(0)
    for i in range(len(units)):
        units[i] = units[i].replace("_", " ")
    regions = ilines[2].split(" ")[1:]
    start = ilines[3].split(" ")[1]
    maximum = ilines[4].split(" ")[1]
    regen_chance = ilines[5].split(" ")[1]
    limited_recruitment_unit_pool_list.append(UnitPoolLR(pool, units, regions, start, maximum, regen_chance))
    
class FactionWideLimitedUnit:
    def __init__(self, pool, units, factions, hidden_res, limit):
        self.pool = pool
        self.units = units
        self.factions = factions
        self.hidden_res = hidden_res
        self.limit = limit
        
    def printtofile1(self, file):
        for faction in self.factions:
            print('\tfor_each\tsettlement in faction "'+faction+'"', file = file)
            print("\t\tadd_hidden_resource local "+self.hidden_res, file = file)
            print("\tend_for", file = file)
        print("\tdeclare_persistent_counter "+self.pool+"_"+self.factions[0], file = file)
        print("\tset_counter "+self.pool+"_"+self.factions[0]+" 0", file = file)

    def printtofile2(self, file):
        for faction in self.factions:
            for unit in self.units:
                print("\tmonitor_event\tUnitTrained UnitType "+unit, file = file)
                print("\t\t&& FactionType "+faction, file = file)
                print('\t\tif\tI_CompareCounter '+self.pool+'_'+self.factions[0]+' = '+self.limit, file = file)
                print('\t\t\tconsole_command destroy_unit local_settlement "'+unit+'" 1 "soldier_count\n\t\tend_if"', file = file)
                print('\t\tif\tI_CompareCounter '+self.pool+'_'+self.factions[0]+' < '+self.limit, file = file)
                print('\t\t\tinc_counter '+self.pool+'_'+self.factions[0]+' 1\n\t\tend_if\n\tend_monitor', file = file)
        print('\tmonitor_event\tNewTurnStart TrueCondition', file = file)
        print('\t\tif\tI_CompareCounter '+self.pool+'_'+self.factions[0]+' < '+self.limit, file = file)
        for faction in self.factions:
            print('\t\t\tfor_each\tsettlement in faction "'+faction+'"\n\t\t\t\tadd_hidden_resource local '+self.hidden_res+'\n\t\t\tend_for', file = file)
        print('\t\tend_if\n\t\tif\tI_CompareCounter '+self.pool+'_'+self.factions[0]+' >= '+self.limit, file = file)
        for faction in self.factions:
            print('\t\t\tfor_each\tsettlement in faction "'+faction+'"\n\t\t\t\tremove_hidden_resource local '+self.hidden_res+'\n\t\t\tend_for', file = file)
        print('\t\tend_if\n\tend_monitor', file = file)
        for faction in self.factions:
            print('\tmonitor_event\tGeneralCaptureSettlement TrueCondition', file = file)
            print('\t\t&& FactionType '+faction, file = file)
            print('\t\tif\tI_CompareCounter '+self.pool+"_"+self.factions[0]+' < '+self.limit, file = file)
            print('\t\t\tadd_hidden_resource local '+self.hidden_res+"\n\t\tend_if", file = file)
            print('\t\tif\tI_CompareCounter '+self.pool+"_"+self.factions[0]+' >= '+self.limit, file = file)
            print('\t\t\tremove_hidden_resource local '+self.hidden_res+"\n\t\tend_if", file = file)
            print('\tend_monitor', file = file)
         
def unit_pool_limited_factionwide(ilines, unit_pool_limited_factionwide_list):
    pool = ilines[0].split(" ")[1]
    units = ilines[1].split(" ")[1:]
    hidden_res = ilines[2].split(" ")[1]
    i = 3
    while ilines[i].startswith("factions"):
        factions = ilines[i].split(" ")[1:]
        limit = ilines[i+1].split(" ")[1]
        unit_pool_limited_factionwide_list.append(FactionWideLimitedUnit(pool, units, factions, hidden_res, limit))
        i += 2
    
print("Enter input file")
ifilename = filedialog.askopenfilename()
ifile = open(ifilename, 'r')
ilines = ifile.readlines()
ifile.close()
print("Enter output file")
ofilename = filedialog.askopenfilename()
ofile = open(ofilename, 'w')

for i in range(len(ilines)):
    ilines[i] = ilines[i].replace("\n", "")
    while ilines[i].startswith("\t") or ilines[i].startswith(" "):
        ilines[i] = ilines[i][1:]
    while ilines[i].endswith("\t") or ilines[i].endswith(" "):
        ilines[i] = ilines[i][:1]

isize = len(ilines)      
for i in range(isize):
    if ilines[isize - i - 1] == "" or ilines[isize - i - 1].startswith(";"):
        ilines.pop(isize - i - 1)
        
nextline = ilines[0]
nextlineindex = 0
dummy_unit_list = []
unit_regeneration_list = []
limited_recruitment_unit_pool_list = []
unit_pool_limited_factionwide_list = []

def nextlinestartswith(line, l):
    for i in l:
        if line.startswith(i):
            return True
    return False

function_list = ["random_unit_group_from_unit", "unit_regeneration", "limited_recruitment_unit_pool", "unit_pool_limited_factionwide", "end"]

while nextline != "end":
    if nextline.startswith("random_unit_group_from_unit"):
        nextlineindex += 1
        nextline = ilines[nextlineindex]
        lines = []
        while not (nextlinestartswith(nextline, function_list)):
            lines.append(nextline)
            nextlineindex += 1
            nextline = ilines[nextlineindex]
        lines.append("end")
        random_unit_from_unit(lines, dummy_unit_list)
    elif nextline.startswith("unit_regeneration"):
        nextlineindex += 1
        nextline = ilines[nextlineindex]
        lines = []
        while not (nextlinestartswith(nextline, function_list)):
            lines.append(nextline)
            nextlineindex += 1
            nextline = ilines[nextlineindex]
        lines.append("end")
        unit_regeneration(lines, unit_regeneration_list)
    elif nextline.startswith("limited_recruitment_unit_pool"):
        nextlineindex += 1
        nextline = ilines[nextlineindex]
        lines = []
        while not (nextlinestartswith(nextline, function_list)):
            lines.append(nextline)
            nextlineindex += 1
            nextline = ilines[nextlineindex]
        lines.append("end")
        limited_recruitment_unit_pool(lines, limited_recruitment_unit_pool_list)
    elif nextline.startswith("unit_pool_limited_factionwide"):
        nextlineindex += 1
        nextline = ilines[nextlineindex]
        lines = []
        while not (nextlinestartswith(nextline, function_list)):
            lines.append(nextline)
            nextlineindex += 1
            nextline = ilines[nextlineindex]
        lines.append("end")
        unit_pool_limited_factionwide(lines, unit_pool_limited_factionwide_list)
    if nextline == "":
        nextlineindex += 1
        nextline = ilines[nextlineindex]
        
print("script", file = ofile)
for i in unit_pool_limited_factionwide_list:
    i.printtofile1(ofile)

for i in limited_recruitment_unit_pool_list:
    i.printtofile1(ofile)

for i in range(len(dummy_unit_list)):
    print("\tfor_each\tsettlement in world\n\t\tdeclare_counter local_region_number" + str(i), file = ofile)
    for j in dummy_unit_list[i][1]:
                   j.printtofile1(ofile, i)
    print("\t\tstore_counter local_region_number"+str(i)+" settlement l_region_number"+str(i), file = ofile)
    print("\tend_for", file = ofile)
for i in range(len(dummy_unit_list)):
    print("\tmonitor_event\tUnitTrained UnitType " + dummy_unit_list[i][0], file = ofile)
    print('\t\tconsole_command destroy_unit local_settlement "' + dummy_unit_list[i][0] + '" 1', file = ofile)
    print("\t\tdeclare_counter region_id\n\t\tretrieve_counter l_region_number" + str(i) + " settlement region_id", file = ofile)
    for j in dummy_unit_list[i][1]:
        j.printtofile2(ofile, i)
    print("\tend_monitor", file = ofile)

for i in unit_regeneration_list:
    i.printtofile(ofile)

for i in limited_recruitment_unit_pool_list:
    i.printtofile2(ofile)
    
if len(limited_recruitment_unit_pool_list) != 0:
    print("Enter instruction file")
    nfilename = filedialog.askopenfilename()
    nfile = open(nfilename, 'w')
    print("For each unit affected by limited_recruitment_unit_pool, it must be stated in export_descr_building.txt that it requires the hidden resource [pool_name]_available to be recruited.\n", file = nfile)
    print("Copy these resource entries to your descr_sm_resources.txt file", file = nfile)
    for i in limited_recruitment_unit_pool_list:
        i.printinstructions(nfile)
    nfile.close()


for i in unit_pool_limited_factionwide_list:
    i.printtofile2(ofile)

print("end_script", file = ofile)
ofile.close()