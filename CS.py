from leftovers import Course, Requirement

class Courses(object):
    def __getattribute__(self, key):
        return Course(key)

c = Courses()

ENGLISH = Requirement([c.ENGL1101, c.ENGL1102], 2)
HUMANITIES = Requirement([ENGLISH], 1, additional_hours=6)

ISYESTAT = Requirement([c.ISYE2027, c.ISYE2028], 2)
PROBSTAT = Requirement([c.MATH3215, c.MATH3670, c.ISYE3770, c.CEE3770, c.ISYESTAT], 1)
MATH = Requirement([c.MATH1551, c.MATH1552, c.MATH1554, c.MATH2550, c.MATH3012, PROBSTAT], 6)

EAS = Requirement([c.EAS1600, c.EAS1601, c.EAS2600], 2)
CHEM = Requirement([c.CHEM1310, c.CHEM1211K, c.CHEM1212K], 2)
BIO = Requirement([c.BIO1220, c.BIO1510, c.BIO1520], 2)
OTHERSCI = Requirement([c.EAS1600, c.EAS1601, c.EAS2600, c.CHEM1310,
                        c.CHEM1211K, c.CHEM1212K, c.BIO1220, c.BIO1510, 
                        c.BIO1520], 1)

PHYS = Requirement([c.PHYS2212, OTHERSCI], 2)
SCISEQ = Requirement([PHYS, CHEM, EAS, BIO], 1)
SCIENCE = Requirement([c.PHYS2211, SCISEQ], 2)

SOCIALSCI = Requirement([c.HIST2111, c.HIST2112, c.POL1101, c.PUBP3000,
                         c.INTA1200], 1, additional_hours=9)

ETHICS = Requirement([c.CS4001, c.CS4002], 1)
JUNIOR_DESIGN = Requirement([c.CS3311, c.CS3312, c.LMC3432, c.LMC3431], 4)
HEALTH = Requirement([c.APPH1040, c.APPH1050], 1)
MISC = Requirement([HEALTH, JUNIOR_DESIGN, ETHICS], 3)

CORE = Requirement([HUMANITIES, MATH, SCIENCE, SOCIALSCI, MISC], 5)

DMATH = Requirement([c.CS2050, c.CS2051], 1)
ALG = Requirement([c.CS3510, c.CS3511], 1)
ALG_FUND = Requirement([c.CS3240, ALG], 1)
BUILD_DEVICES = Requirement([c.CS3651, c.ECE4180], 1)

RW_DEVICES = Requirement([c.CS3630, c.CS4261, c.CS4605], 1)

DEVICES = Requirement([c.CS1301, c.CS1331, c.CS1332, DMATH, c.CS2110, c.CS2200,
                       c.CS2340, c.CS3251, c.ECE2031, ALG_FUND, BUILD_DEVICES,
                       RW_DEVICES], 12, additional_hours=6)

INTROINFO = Requirement([c.CS3251, c.CS4235, c.CS440], 2)
ADVINFO = Requirement([c.CS4237, c.CS4251, c.CS4255, c.CS4261, c.CS4270,
                       c.CS4365, c.CS4420, c.CS4440, c.CS4675], 1)

INFONETWORKS = Requirement([c.CS1301, c.CS1331, c.CS1332, DMATH, c.CS2110,
                            c.CS2200, c.CS2340, ALG, INTROINFO, ADVINFO],
                            10,additional_hours=6)

COMPLEX = Requirement([c.CS3240, c.CS4510], 1)
EMBODIED = Requirement([c.CS3630, c.CS3790, c.PSYC3040], 1)
APPROACHES = Requirement([c.CS4476, c.CS4635, c.CS4641, c.CS4649, c.CS4650,
                          c.CS4731], 2)
INTELLIGENCE = Requirement([c.CS1301, c.CS1331, c.CS1332, DMATH, c.CS2110,
                            c.CS2340, ALG, c.CS3600, COMPLEX, EMBODIED,
                            APPROACHES], 11, additional_hours=6)
                # Also requires PSYC 1101, I'll figure that out

MEDIA = Requirement([], 0)
MODSIM = Requirement([], 0)
PEOPLE = Requirement([], 0)
SYSARCH = Requirement([], 0)
THEORY = Requirement([], 0)

THREADS = Requirement([DEVICES, INFONETWORKS, INTELLIGENCE, MEDIA, MODSIM,
                       PEOPLE, SYSARCH, THEORY], 2)
