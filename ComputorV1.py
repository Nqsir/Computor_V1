import sys
import re
import argparse
import logging


EQUAL = 0
SIGN = 1
NUMBER = 2
POWER = 3

OK = 0
ERROR = 1
INF = 2


def dumb_func():
    print("ssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssyyyyyyyyyyyssssyyyyyyyyyyssssssssssssssssssyyyyyyyyyyyyyyyyyyyyyyyysyyyyysssssysssssssssssssssssssssssssssssssyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyy\n"
          "sssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssddddddddddddddddydddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddhhysssssshmddddddddddddddmmmmmmmmmmmmddmdmmmmmmmmdmmddddhhyysssssssyhmNNMMMMMMMMMMMMMNNmdhyysysysysssssysssssssssssssssssssssssssssssssyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyy\n"
          "sssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssNMMNmmmmmmmmmNMMNMMMmmmmmmmmmmMMMMmmmmmmmmmmmmMMMmmmmmmmmmmmmMMMMNmmmmmmmmmmmmmmmMMMMMNmmmmmmmmmmmmmmmMMMMNmmmmmmmmmmmmmmmNNMMMMMMNdyssNMMNmmmmmmmmmmmmmmmmmmdMMMMmmmmmmmmmmmmmmmNNNMMMMMMmhssshmMMMMMmhyo+++++ooyhmMMMMNmysysyysssssysssssssssssssssssssssssssssssssyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyy\n"
          "sssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssNMMo`````  ``:NMMMMN ```` `` -MMMM``````` ```-MMM.   `  `  `.MMMMy``````````````:MMMMM:``````` `` `` -MMMMs````        ``````-:ohNMMNhsNMMs`` ````````````````hMMM`` `     `````````.-:odMMMNymMMMMd+.`            `./yNMMNhyyyysssssysssssssssssssssssssssssssssssssyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyy\n"
          "sssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssNMMo          sMMMMN         .MMMM`          .MMM.          .MMMMs              `NMMMm.              .MMMMs                      .yMMMhNMMo                   hMMM`                      -dMMMMMMm:`                   .sMMNysyysssyyssssssssssssssssssssssssssssssssyyyyyyyyssyyyyyyyysssyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyy\n"
          "sssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssNMMo          .mMMMN         .MMMM`          .MMM.          .MMMMs               yMMMh               .MMMMs                       `+MMNNMMo                   hMMM`                       `hMMMMN-                       yMMhyyysssyyssssssssssssssssssssssssssssssssyyyyyyyyssyyyyyyyysyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyy\n"
          "sssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssNMMo           /MMMN         .MMMM`          -MMM.          .MMMMs               +MMMo               .MMMMs           -::`          hMMMMMo                   hMMM`          `::.          .NMMMs          :hdo`         :MMdsyyyssssssssssssssssssssssssssssssssyyssyyyyyyyyssyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyy\n"
          "sssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssyhhhMMM+           `yMMN         .MMMM`          .MMM.          .MMMMs               .MMM:               .MMMMs           hMNy`         /MMMMMs           +sssssssmMMM`          .MNN:          dMMM:          NMMM-         `MMdysyyssssssssssssssssssssssssssyyyysyyyssyyyyyyyyssyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyy\n"
          "ssssssssssssssssssssssssssssssssssssssssssssssssssssssssssyhhddddNMMo            .mMN         .MMMM`          .MMM.          .MMMMs                dMN`               .MMMMs           hMMM`         .MMMMMs           hMNNNNNNNMMM`          .MMMs          yMMM-          NMMM-          NMdysyyssyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyy\n"
          "sssssssssssssssssssssssssssssssssssssssssssssssssssssssssyhddddddNMMo             +MN         .MMMM`          .MMM.          .MMMMs                oMh                .MMMMs           hMMM`         .MMMMMs           hMmyhyyyhMMM`          .MMMs          yMMM-          +NMM+:--:--:--:NMdysyyssyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyy\n"
          "yysssyyyysssssssyyysssssssssssssssssssssssssssssssssyyyhhddddddddMMMo             `dN         .MMMM`          .MMM.          .MMMMs                -Mo      `         .MMMMs           hMMm`         :MMMMMs           hMNmmdddmMMM`          .MMMo          hMMM+           -smNNNNNNNNNNNMMdsyyyssyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyy\n"
          "yyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyhhhddddddmmdddddhhNMMo              -N         .MMMM`          .MMM.          .MMMMs          -      m:     `-         .MMMMs           ohy:         `hMMMMMs           smmmmmmmMMMM`          .hyo`         .NMMMd`            `:sdMMMMNdhhhhyyyyyssyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyysyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyy\n"
          "hhhhhhhhhhhhhhhhyyhhhhyyyyyyyyyyyyyyyyyhhhhhhddddddddddmmmmmmmdddNMMo               +         .MMMM`          .MMM.          .MMMMs          o      s`     /:         .MMMMo                    `.-+dMMNNMMo           `.`....:MMMM`                      `-hMMMMMy`              `:smMMMNdyyyyyssssssssyyyyssssssssssssssssssssyyyyyssyyyyyyyyyssyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyy\n"
          "hhhhhhhhhhhhhyyyyyyyyyhhyyyyyyyyyyyyyhhhdddddddddddddmmmddhddmmmmMMMo               `         .MMMM`          .MMM.          .MMMMs          h`     .      s:         .MMMMo                    ./ymMMMNNMMo                  .MMMM`                   `:ohNMMMNMMMd/`               ./hNMMNhysyssssssssyyyyssssssssssssssssssssyyyyyssyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyy\n"
          "yyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyhhddddddddddddddddddyo/+oosyhNMM+                         .MMMM`          .MMM.          .MMMMs         `d-            m:         .MMMMo                       .+mMMMMMo                  .MMMM`                    `-+hMMMdmMMMNdo-`              `:hMMMhyyyyyyyyssyyyyssssssssssssyyyyyyyyyyyyyssyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyy\n"
          "yyyyyyyyyyyyyyyyyyyyyyyyyyyysssssyyhddddddddddddhhhddmhs//://////NMM+         .               .MMMM`          .MMM.          .MMMMs         `mo           .N:         .MMMMo           oys:          -mMMMMs                  .MMMM`          .yy+`        `oMMmyhNMMMMNh+-              `sMMNyyyyyyyyysyyyyssssssssyyyyyyyyyyyyyyyyyssyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyy\n"
          "yysyyyyyyyyyyyyyysssssssssssssssyyhdddddddddddhhhhhdmho/::::::://mMMo         o.              .MMMM`          .MMM.          .MMMMs         `mh           /M/         .MMMMo           hMMN`          oMMMMs           ohhhhhhdMMMM`          .MMM/         `dMMNNNMMMMMMMNh+.            `dMMhyyyyyyyyssssssssyysssssssyyyyyyyyyyyyyyyyyyssssyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyy\n"
          "ssssyyyyyyssssyysssssssssssssssyhddddddddddddhhyhhdmh+::::::::///mMMo         ys              .MMMM`          .MMM.          .MMMMs         `mN`          yM/         .MMMMs           hMMM`          -MMMMs           hMMNNNNNNMMM`          .MMMs          yMMMdoo+o++o+o+hmy:`          /MMdyyyyyyyyssssssssyysssyyssyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyy\n"
          "ssssssssssssssssssssssssssssssyhdddddddddddddhyyhdmds/::::::::://mMMo         yN-             .MMMM`          .MMM.          .MMMMs         `NM:          mM/         .MMMMs           hMMM`          .MMMMs           hMmyyyyyhMMM`          .MMMs          sMMMy          oMMNo          .MMdyyyyyyyyssssssssyssssyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyy\n"
          "ssssssssssssssssssssssssssssssyhdddddddddddddhyhdmmh+:/::::::::::mMMo         yMh`            .MMMM.          .MMM.          .MMMMs         `NMo         -NM/         .MMMMs           hMMM`          -MMMMs           hMNhhhhhdMMM`          .MMMs          sMMMy          oMMMN`          MMdyyyyyyyyssssssssysssyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyy\n"
          "sssssssssssssssssssssssssssssyhdmdddddddddddddhddmms///::::::::::mMMo         yMM/            .MMMM-          -MMM.          -MMMMs         `NMd         +MM/         .MMMMs           hMMN`          -MMMMs           hMMMMMMMMMMM`          .MMMs          sMMMh          sMMMM.          MMhyyyyyyyyyyyssssyyyyyyyyyyyyyyyyyyyyssyyssyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyy\n"
          "ssssssssssssssssssssssssssssshddmdddddddddddddddmmdo///:::::::::/mMMo         yMMm`           .MMMM/          .NMm`          /MMMMs         `NMN.        yMM+         .MMMMs           ymdo           :MMMMs           -::::::::mMM`          .MMMs          sMMMm`         /MMMm`         .MMdyyyyyyyyyssssssssyyyyyyyyyyyyyyyyyysyyyysyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyy\n"
          "ssssssssssssssssssssssssssssyhddddddddddddddddddmmh+////:::::://+NMMo         yMMMo           .MMMMd`         `:+:          `dMMMMs         `NMM:       `mMM+         .MMMMs           ```            oMMMMs                    dMM`          .MMMs          sMMMM/         `/o+.          +MMdyyyyyyyyyssssssssyyyyyyyyyyyyyyyyyysyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyy\n"
          "ssssssssssssssssssssssssssssyhddddddddddddddddddmdy+////:///+osyhNMMo         yMMMN.          .MMMMMy`                     `yMMMMMs         `MMMs       -NMM+         .MMMMs                         .mMMMMs                    dMM`          .MMMs          sMMMMm-                      -NMMyyyyyyyyyyyssssssyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyy\n"
          "ssssssssssssssssssssssssssssyhddddddmdddddddddddmdo/////////++oooNMMo         yMMMMy          .MMMMMMm/`                 `/mMMNNMMs         `MMMd`      +MMM+         .MMMMs                       `-dMMMMMs                    dMM`          .MMMs          sMMMMMNs.`                 .oNMMmysyyyyyyyssssyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyy\n"
          "ssssssssssssssssssssssssssssyhdmddddmmmddddddddmdh+//////::/+++//NMMs..-......hMMMMM:.........:MMymMMMMNy+-.`      ```.:smMMMmymMMy.........-MMMN:......hMMMs.......-.:MMMMy................--::/+sdMMMNNMMs....................dMM-..-.......:MMMy..........yMNdMMMMNho:.```     ``.:ohNMMMmyyyyyyyyyyssssyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyy\n"
          "ssssssssssssssssssssssssssssyhdmdddmmmmddddddddmds+////:////+/::-mNMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMysyhmMMMMMNmdhhyyhhdNMMMMNmhssmMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMNmhsNMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMmsydNMMMMMNmdhhyyhhdmNMMMMNmhyyyyyyyyyyysyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyy\n"
          "ssssssssssssssssssssssssssssyhdmddmdmmmdddddddddho/////:/:////---+++ooohmmmNNNmmhsssyyhdhyoosydmmddds/shdmNNNNNNNmmNNmmdhysssssyhhhhhhhhhhhhhhyhhhhhhhhhhhhhhhhhhhhhhhhhhhhyhhhhhhhhhhhhhhhhhhhhhhyyssssyhhhhhhhhhhhhhhhhhdddhhhhhhhhhhhhhhhdhhhhhhhhhhhhhhyhhhyssssyhdmmNNNNNNNNNNNmmdhyyyyyyysyyyyyyysyyyyysssyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyy\n"
          "ssssssssssssssssssssssssssssyhmmddddmmmmmmdddddds//////:::://:----::://odmmmNmmdyo//++sys+/:/yddmmmmms+syhysssssssssssssssssssssssssssssssssssssssssssssssssyyyyyyyysyysssssssssssssssssssssssssssssssssssssssssssssssssyyyyyyyyyyysssssyyyyyyyyyyyyyyssssssssssssssyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyssyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyy\n"
          "ssssssssssssssssssssssssssssyhddddmmmmmmmmmmdhhho///://::::///::-:::://+sdmmmmmds+///+sys+///sdmmNmNmhoosyysssssssssssssssssssssssssssssssssssssssssssssssssyyyyyyyyyyssssssssssssssssssssssssssssssssssssssssssssssssssyyyyyyyyyyysssssyyyyyyyyyyyyyyysssssssssssssyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyssyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyy\n"
          "ssssssssssssssssssssssssssssshddhhysssyhhhhddhhyo///::::::::////::::///+osydddhyo//://osso///+ydmmmmmyoossssssssssssssssssssssssssssssssssssssssssssssssssssyyyyyyyyyysssssssssssssssssssssssssssssssssssssssssssssssssyyyyyyyyyyyysssssyyyyyyyyyyyyyyysssssssssssssyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyssyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyy\n"
          "sssssssssssssssssssssssssssssyhs+////:://++yddhyo///::::::::://///////++ossssyyo+//::/+sys+//++shhddysoossssssssssssssssssssssssssssssssssssssssssssssssssssyyyyyyyyyysssssssssssssssssssssssssssssssssssssssssssssssssyyyyyyyyyyyysssssyyyyyyyyyyyyyyssssssssssssssyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyssyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyysyyyyyyyhhhyyyyyyyyyyyyyyyyyyyyy\n"
          "sssssssssssssssssssssssssssssso+o++///+////odddyo///::::::::::///////++ossssso++/:/:://+ssso++oosssssssoosssssssssssssssssssssssssssssssssssssssssssssssssssyyyyyyyyyysssssssssssssssssssssssssssssssssssssssssssssssssyyyyyyyyyyyysssssyyyyyyyyyyyyyyssssssssssssssyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyssyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyysoooyhhhhdddhyyyyyyyyyyyyyyyyyyyy\n"
          "ssssssssssssssssssssssssssssso+o+/::::////:+hddho///:::::::::::///////+++++++///////:://+ossooossyysssoooossssssssssssssssssssssssssssssssssssssssssssssssssyyyyyyyyyysssssssssssssssssssssssssssssssssssssssssssssssssyyyyyyyyyyyyyssssyyyyyyyyyyyyyyssssssssssssssyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyysyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyss+///shddddddhyyyysyyyyyyyyyyyyyyy\n"
          "ssssssssssssssssssssssssssssso++//:::://///+hddho//////::::::::////++++++++++++////::////+oooo+++++++++++oosssssssssssssssssssssssssssssssssssssssssssssssssyyyyyyyyyysssssssssssssssssssssssssssssssssssssssssssssssssyyyyyyyyyyyyysssyyyyyyyyyyyyyyyysssssssssssssyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyysyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyso+////+ossyhhhyyyyyyyyyyyyyyyyyyyyyy\n"
          "ssssssssssssssssssssssssssssso++/:////+//:/odddho///////:::::::///++++++++++++++//////////++ooo++++++++++oosssssssssssssssssssssssssssssssssssssssssssssssssyyyyyyyyyysssssssssssssssssssssssssssssssssssssssssssssssssyyyyyyyyyyyyyyssyyyyyyyyyyyyyyyyssssssssssssyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyysyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyso+/::/++oosssyyyyyyyysooosyyyyyyyyyyyy\n"
          "sssssssssssssssssyysssssssssso+//://oo++//+odddhs////////::::::///+++ooooooooo++//::////////++oooo+ooooooooossssssssssssssssssssssssssssssssssssssssssssssssyyyyyyyyyysssssssssssssssssssssssssssssssssssssssssssssssssyyyyyyyyyyyyyyssyyyyyyyyyyyyyyyysssssssssssssyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyso+/://+ooooosyyyyyysso+///+yyysyhhhhhyyy\n"
          "ssssssssssssssssssssssssssssso+//:/+++////+odmdhs+//////////://///++oooooooooo++//::/::://///++++oooooooooosssssssssssssssssssssssssssssssssssssssssssssssssyyyyyyyyyyssssssssssssssssssssssssssssssssssssssssssssssssssyyyyyyyyyyyysssyyyyyyyyyyyyyyyyssssssssssssyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyysssyssssyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyso+/::/+oooossyyyysysso++////shdhhdhhdddyyy\n"
          "sssssssssssssssssssssssssssssso+/:////////++yhys++///////////////+++oooooooooo++//::/:::://///++osssooosssssssssssssssssssssssssssssssssssssssssssssssssssssyyyyyyyyyysssssssssssssssssssssssssssssssssssssssssssssssssyyyyyyyyyyyyyyssyyyyyyyyyyyyyyyyssssssssssssyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyysssssssssssssssssssyyyyyyyyyyyyyyyyyyyyyyyysyso/::/++oooossyyyysssoo++++++osyddddddddhyyy\n"
          "ssssssssssssssssssssssssssssssso/:://///////oo++///////////////++++ooooooooooo++///////++ooossyyhhysssssssssssssssssssssssssssssssssssssssssssssssssssssssssyyyyyyyyyyyyyysssssssssssssssssssssssssssssssssssssssssssssyyyyyyyyyyyyyyssyyyyyyyyyyyyyyyyssssssssssssyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyysssssssssssssssssssyyyyyyyyyyyyyyyyyyyyyyyyss/:::/+++oossyyyyssoooo++ooooosssyhdddhhyyyyy\n"
          "sssssssssssssssssssssssssssssssso/::////////+++//////////////++++++oooooooo+++++//+oossyyyyyhhhhhyyssssyyyyyssssssssssssssssssssssssssssssssssssssssssssssssyyyyhhhyyyyyyhhhhyyyyyyysssssssssssssssssssssssssssssssssssyyyyyyyyyyyyyyssyyyyyyyyyyyyyyyyssssssssssssyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyssssssssssssssssssssyyyyyyyyyyyyyyyyysyyyyyyo/-:/++oooossyyssooo+++oooooossssyyyyyyyyyyyyy\n"
          "ssssssssssssssssssssssssssssssssso//:////////++//////////////++++++ooooooo++++++++ossyyhhhhhhhhhyyssssyyyyyysssssssssssssssssssssssssssssssssssssssssssssyyyhhhhhys+//oyhhhhyyyyhhhhhyyssssssssssssssssssssssssssssssssyyyyyyyyyyyyyssyyyyyyyyyyyyyyyyyssssssssssssyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyssyysysssssssssssssssssssssssyyyyyyyyyyyyyyyyyyyyhyyyys://++ooossysso++++++oooooosssyyyyyyyyyyyyyyyy\n"
          "sssssssssssssssssssssssssssssssssso+/:::::///+/////////////////+++++++++++++++++++++oossyyyyyyyyssssssyyyyyyssssssssssssssssssssssssssssssssssssssssssyyyhhhhhyyss+///+osssysyssssyhhhhysssssssssssssssssssssssssssssssyyyyyyyyyyyyyssyyyyyyyyyyyyyyyyyssssssssssssyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyysssssysssssssssssssssssssssssssyyyyyyyyyyyyyyyyyyyyhyyyyo/++oooossso++///+++ooooosssyyyyyyyyyyyyyyyyyy\n"
          "ssssssssssssssssssssssssssssssssssso+//::://++////////////////////+++++++++///////+++oooosssssssssssssssyyysssssssssssssssssssssssssssssssssssssssssyyyyyhhhyo++//////+oosyyso+oooosyhhhyyssssssssssssssssssssssssssssyyyyyyyyyyyyyyssyyyyyyyyyyyyyyyyyssssssssssssyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyssssssssssssssssyyyyyyyyyyyyyyyyyyysyyyyyhyo+++ooossso+////+++oooossssyyyyyyyyyyyyyyyyyyyy\n"
          "ssssssssssssssssssssssssssssssssssssso++///+++///////////////////////+++++//////+++++++oooossssssssssssssssssssssssssssssssssssssssssssssssssssssssyysyhhyso++++/////++ooss+//:////+ooyhhyysssssssssssssssssssssssssssyyyyyyyyyyyyyyssyyyyyyyyyyyyyyyyyssssssssssssyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyysyyyyyyyyyyysssssssssssssyyyyyhhhhhyyyyyyyyyys//+syhhhyso+ooso+////++++++ooooo+///+oosyyyyyyyyyyyyyyy\n"
          "ssssssssssssssssssssssssssssssssssssssssssoso+//////////////////////////++/////+++++oooooooossssssssssssssssssssssssssssssssssssssssssssssssssssssyysyhhyooo++/+//////++oo+::-/shhyo+/+ssyyysssssssssssssssssssssssssssyyyyyyyyyyyyyysysyyyyyyyyyyyyyyyssssssssssssyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyssssssssssyyyssyhhdddyyyyysyss+/-.-/oyhhdddyyso+///++++++ooo+/::---:://+osyyyyyyyyyyyyy\n"
          "sssssssssssssssssssssssssssssssssssssssyhmdmho/////////////////////++++++/////+++++ooo+ooooosssyyyyysssssssssssssssssssssssssssssssssssssssssssssyysshhyso+/:/::/++++//+oo/--:+ydmdy++/++oshyssssssssssssssssssssssssssyyyyyyyyyyyyyysysyyyyyyyyyyyyyyyssssssssssssyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyysssssssyyhhhhdddmmdhyyyysso/:---:/+osyhddddhyoo+++++oooo+/:::::::::///+oyyyyyyyyyyyyy\n"
          "ssssssssssssssssssssssssssssssssssssssssydmNms+///////////////////++++++///++oossssssssssyyyyhhddhhhhyssssssssssssssssssssssssssssssssssssssssssyhsoyhys+/::-:::+yhdyo/:/++/::/+oossoooo++oyhysssssssssssssssssssssssssyyyyyyyyyyyyyysysyyyyyyyyyyyyyyyssssssssssssyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyssssssyyyhdddmmmddhyyyyo/:--:://+++oosyhdddddhysooooo++///++/::://////osyyyyyyyyyyyy\n"
          "sssssssssssssssssssssssssssssssssssssssssyhmmho+//////////////////+++++++oosssssssssssssyyyyyyhdddmmdhyyysssssssssssssssssssssssssssssssssssssssyhs+yhyo/:----::oyddhs/::/++///+oossssoo++ooyhyssssssssssssssssssssssssyyyyyyyyyyyyyysysyyyyyyyyyyyyyyyssssssssssssyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyysyyyyyyhdddhhhhhyyyo/:---:/++oooooosssyhdddddhyyo+//+ooso+::://++++ossyyyyyyyyyyy\n"
          "ssssssssssssssssssssssssssssssssssssssssssshddo+//////////////////++oooosyyysssssssssssssyyyyyhhddmmmhyyyssssssssssssssssssssssssssssssssssssssshhy+oyy+/----:///+ooss+::://+++++ooooo++++++osyssssssssssssssssssssssssyyyyyyyyyyyyyyssyyyyyyyyyyyyyyyysssssssssssssyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyhhyyys+//////+oooooooosooosyhddddhhssooossoooossoooooo++syyyyyyyyyy\n"
          "ssssssssssssssssssssssssssssssssssssssssssssyhs++/////////////////+osssooooo++++++++ooooossssssyyhhdhhyyyssssssssssssssssssssssssssssssssssssssyhdyo+++/:::::///+ooss+/::::://+///////++++++oosssssssssssssssssssssssssyyyyyyyyyyyyysssyyyyyyyyyyyyyyyyyssssssssssssyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyo+////+ossssssssoooooosyhdddddhyyyyyyyyhhhhysoo+/osyyyyyyyyy\n"
          "ssssssssssssssssssssssssssssssssssssssssssssssso+/+///////////////++ooo+///////////+++++ooooooossssssssyssssssssssssssssssssssssssssssssssssssyyhhhs+/:::////+++ooo+/:::/:::/++++////++++++++oossssssssssssssssssssssssyyyyyyyyyyyyysssyyyyyyyyyyyyyyyyyssssssssssssyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyhhyyyyyo/:::/+sssssssooo+++++oosyhdhddhhhyysyhdddhysoooosyyyyyyyyy\n"
          "ssssssssssssssssssssssssssssssssssssssssssssssso++//////////////////++/////////////+++++++++ooooooooossssssssssssssssssssssssssssssssssssssssyyyhhhho//::::://////::::::::/+syysoo+//++++++ooooosssssssssssssssssssssssyyyyyyyyyyyyysssyyyyyyyyyyyyyyyyyssssssssssssyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyhhhyyyyys+::::+ssssssssoo++++++++oosyhhdddhhhhdddhhyssssssyyyyyyyyy\n"
          "sssssssssssssssssssssssssssssssssssssssssssssssso+++////////////////////////////////++++++++++ooooooooossssssssssssssssssssssssssssssssssssssyyhhhhho/::::::::::::::::::/+syhhyyso+//++oooooooooossssssssssssssssssssssyyyyyyyyyyyyyyssyyyyyyyyyyyysyyyssssssssssssyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyhhyyyyo//::+ssssssssooo+++++++++++oshhdddhhddhyyyyysyyyyyyyyyyyy\n"
          "ssssssssssssssssssssssssssssssssssssssssssssssssoo++///////////////////////////////++++++++++oooooooooosssssssssssssssssssssssssssssssssssssssyhhhhhs/::::::::::::::::::/oosoo+++++++oooooooooo+oosssssssssssssssssssssyyyyyyyyyyyyyysyyyyyyssoo+++ooooosssssssssssyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyso+//+syysyysssoo+++++/+++++oooosyhysosyyyyyyyyyyyyyyyyyyyy\n"
          "ssssssssssssssssssyyyssssssssssssssssssssssssssssso+++/////////////////////////////++++++++++ooooooooossssssssssssssssssssssssssssssssssssssssyhhddhs/:/::////////::::::::///+ooosoossyyssoooooo+osssssssssssssssssssssyyyyyyyyyyyyyyyyyyyyyo++//+++++++++++ooossssyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyysoo+osyyyyyysssoo+++/////++++ossyyhhysssyyyyyyyyyyyyyyyyyyy\n"
          "ssssssssssssssssssyyyyyysssssssssssssssssssssssssssoo+++++++++////////////////////++++++++++oooooooooosssssssssssssssssssssssssssssssssssssssssyhddds///////////////:::::/+++++++++ooshddyo+ooo+++ossssssssssssssssssssyyyyyyyyyyyyyyyyyyyys+++/++oooooooooo+++++ooooosyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyssyyyyyyyyssssssyyyyyysssoo++/////++++oossyhhdddhyyyyyyyyyyyyyyyyyyyy\n"
          "ssssssssssssssssssssssssssssssssssssssssssssssssssssssoo+++++++////////////////+/++++++++oooooooosssssssssssssssssssssssssssssssssssssssssssssssshhds//////////////////:::--/+syhdddddddhs+++++++++ossssssssssssssssssyyyyyyyyyyyyyyysyyyyso+++++oooo++oossso+++++++/:/oyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyysssyyyyyyyyssssyyyyyyssoo+++////+++oosssyyhhdddhhyyyyyyyyyyyyyyyyyyy\n"
          "sssssssssssssssssssssssssssssssssssssssssssssssssssssyyssoooooo+++++///////////++++++oooooooosssssssssssssssssssssssssssssssssssssssssssssssssssssyys+//////////+////+o+++shddmmmdmdmmdy+/++++/++++oossssssssssssssssssyyyyyyyyyyyyyyyssys+:+++++ooo++//+osssoo++o++/://oyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyysssssyyyyyyyyyyyyyyyysssoo++++++++oosssyyyyyyyyyyyyyyyyyyyyyyyyyyyyyy\n"
          "ssssssssssssssssssssssssssssssssssssssssssssssssssssssyyyyyssssoooo++++//////+++++++oooooosssssssssssssssssssssssssssssssssssssssssssssssssssssssssyyo//////////////+yhyydmdddddhyssoo+/+o+++++/++++osssssssssssssssssyyyyyyyyyyyyyyysyys+:/+oooooooo+//+syhyyyyyyyyo///+syyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyso+++++osssyyyyyyyyyyyyyysssoo++++oooosyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyy\n"
          "ssssssssyyyyssssyyyssssssssssssssssssssssssssssssssssssyyyyyyyyssssoo++++++++++++oooooossssssyyyyyyyyyssssssssssssssssssssssssssssssssssssssssssssssys+//////::::::::://++ooso+/////+oosoo++++++++++osssssysssssssssssyyyyyyyyyyyyyyssss+/++ooo+++++oosssyhyyyyyysssyoo++osyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyys+:---:/+oosssyyyyyyyyyyysssssooooooossyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyy\n"
          "ssssssssyyyyyyyyyysssssssssssssssssssssssssssssssssssssssyyyyyyyyyyysssoooooooooooossssssyyyyyyhhyyyysssssssssssssssssssssssssssssssssssssssssssssssyso////::/::::::::::::///+++ooooooo+++++++++++++oosssssssssssssssssyyyyyyssooo+++++o++o+ooo+++++osyyyyysoo+syyssyysooosyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyo/:------:/ooossyyyyyyyyyyyysssssssssyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyy\n"
          "ssssssssyyyyyyyyyyssssssssssssssssssssssssssssssssssssoooosssyyyyyyyyyyyyysssssssssyyyyyyyhhhhhhhhyyysssssssssssssssssssssssssssssssssssssssssssssssyys+///::::::::::::::::::////////////////++++++++ossssssssssssssssoo+++++++oooossooooo+++oo+++++osyyyso+++osyhyyhhysossyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyysso/:::------:/++oossyyssyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyy\n"
          "ssssssssyyyyyyyyyyssssssssssssssssssssssssssssssssssssooooooossssyyyyyhhhhyyyyyyyhhhhhhhhhhhhhhhyyyysssssssssssssssssssssssssssssssssssssssssssssssssyso+///::::::::::::::::::::://///////////+++++++oooossssooo++++++++ooosoooooooooooooooooooooooooooooo+++ooshdhhhhysssssyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyss+:-:::::-:::///+oosssyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyy\n"
          "ssyysssyssssssssyysssssssssssssssssssssssssssssssssssso++++++oooossyyyyhhhhhhhhhhhhhhhhhhhhhyyyyysssssssssssssssssssssssssssssssssssssssssssssssssssssss+///:/::::::::::::::::::::::////////+++++++++ooo++++++oooooooooo++++++++oooooooooosssssssoo++++oo++++oosydddhhhsssssyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyso/:----::::::////++osssyyyyyyyyhyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyy\n"
          "yyyyyyyyyyyyyyyyyyyysssssssssssssssssssssssssssssssssso+++++++++ooossyyyhhhhhhhhhhhhhhhhhhhyyssssssssssssssssssssssssssssssssssssssssssssssssssssssssssys++////::::::::::::::::::::::///////+++++o+++ossysssssssoo+++++++++++++++ooooooosssssyysoo+++++oo++oossyhdmmdhyo+++oosyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyysyyyys+/:::::-----:://+/+oosyyyyysssyyhyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyy\n"
          "yyyyyyyyyyyyyyyyyyyyssssssssssssssssssssssssssssssssss++++++++++++oossyyyyhhhhhhhhhhhhhhyyyssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssysso+///::::::::::::::::::::://////++++oooooooosyhhyyyyysssoooo+++++++++++oooooososssyyso++++++oo++oosyyyyhddhyoo++/++syyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyysyyyyyyyo/::::::::-----::/++oosyyyyyyssosyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyy\n"
          "yyyyyyyyyyyyyyyyyyyyyyyyssssssssssssssssssssssssssssys++++++++++++ooossyyyhhhhhhhhhhhhhyyysssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssyso++////::::::::::::::::////+++ooooossssssooshhhhhhhhhyyysssoo+++++++ooooooossssyysso++++oo+++oosyyysyssoooosyhyysssyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyso/::::::::::::::::::/+ossyyyyyssosyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyy\n"
          "yyyyyyyyyyyyyyyyyyyyyyyysssssssssssssssssssssssssssyhs+++++++++++++oossyyyhhhhhhhhhhhhyyyssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssyyyoo+//////:::::::::::///++oooossssyyyssssssyhddhhhhhhhhhhyysoo++++oooooosssssyyyyoo+oooo+++++osyyyyysooshdmmmmmmdddhhyyssyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyys+/::::::::::::::::://////+oosssssosyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyy\n"
          "yyyyyssssssyyyyyyyyyyyyysysssssssssssssssssssoo+++osyso++++//++++++oosssyyyhhhhhhhhhhyyyssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssyhyso+++//////////////+++oosssyyyyyyyyyyssyhdddddhhhhhhhhhhhysooooooooossssyyyyyso+++++oo+++oosyyyyssoshmNmmmmmdysoooooooooosssssyyyyyyyyyyyyyyyyyyyyyyyyyyyyso/::::::::::::::://///////++oosssssssyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyy\n"
          "sssyyyyyyyyyyyyyyyyyyyyysssssssssssssssssssso+/:/+oyhhso+//////++++oosssyyyyhhhhhhhhyyyssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssooooosydhyso+++////////++++oosssyyyyyyyyyyyyyyhhdmmmmmdhhhhhhhhhyysoooooossssyyyyyysso++oo++oo+oooyyyyysosydmmmmmmmdyoooooooooooooooossssyyyyyyyyyyyyyyyyyyyyyyyys+/::::::::::::::///////++++oossyyyysssyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyy\n"
          "sssssysyssyyyyyyyyyyyysssssssssssssssssssooo++/++ssyhddhso+//////+++oosssyyyhhhhhhhyyyyysssssssssssssssssssssssssssssssssssssooosssooooooooossssooooosssssyyddhhyso++++++++oooosssyyyyhhhhhhhyyyhhddmmmmmmmmddddddhyssoooooossssyyysssooooo++ooooo++oosyyyyssshdmmmmmmmdyoooooooooooooooooooossssyyyyyyyyyyyyyyyyyyyys+/:::::::::::::://////+++++oossyyyyysssyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyy\n"
          "sssyyyyyyyyyyyyyyyyyyyysyyysssssssssss+/////++ooshhhhdmdhysso++//+++ooosssyyyhhhhhhyyyhhhyysssssssssssssssssssssssssssssssssooosssoooooo+ooossssssssssysyyyyhddhhhyysooooossssyyyyyhhhhhhhhhhhhhddmmmmmmmmmmmmddhysooooooosssyyssooooooooooooooooo+ossyyyysssydmmmmmmmmdsoooooooooo+++/////////++oossyyyyyyyyyyyyyyso+/::::::::::::::://///+++++oossyyyyyyyssyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyy\n"
          "yyyyyyyyyyyyyyyyyyyyyyyyyyyyysysssysso//::::/+oosyhhhhyyyyysssssooo+oooosssyyyyhhhyyyhhdhhyysssssssssssssssssssssssssssssssso+sys++++++++oooosssssssssssyyyyhhdhhhhhhyyyyyyyyyyhhhhhhhhhhhhddddmmmdmmmmmmdddhyssooooooossssssooo+++oooooooooooo+oooosyyyyyssydmmdmmddmmhsooooooooo+/:::::::::::::::////++ooosssyyyso+/::::::::::::::://///++++ooossyyyhhyyyssyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyysyyy\n"
          "yyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyso+/++++/::::+oosssoooosyyssssyyyssssssssyyyyhhhhhyhhddhhhhyysyysyysyyyyyyyyyyyyyyyyyysyyss+osyo//++oo++oosoosssssssssyyyyhhhhhhhhhhhhhhhhhhhhhddddddddmmmmmmmmmmddddhhyssoooooooossssssooo++++oooooooooooooooooossyyhyyssyhmmdddmddmdyo+++oooo+/:------:::::::::::::::::::://+ooo+/::::::::::::::://///+++++oossyyyhhyyyyssyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyssssss\n"
          "yyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyo+::::/++++/::+syhhyo++oossssssyyyyyhhhhhhhhhhhhhhhhdddddhhhyssyyyyyyyyyyyyyyyyyyyyyyyyyyyysoosyo++oossoooossssssssssyyyyhhhhhhdhhhhhhhhhhhddddddddmmmmmmmdddddhhysssssooooooooossoooo++++++++ooooooooooooooooooossyhhhyysyydmddddmddmdy+++++++/:---------::::::::::::::::::://+++o+/::::::::::::://////+++++oossyyyyhyyyysssyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyssssssssssssss\n"
          "yyyyyyyyyyyyyyyyyyyyyyyyyyyssooo++//:::/+oooosyyhdddyo+ooo+++ooossyhdddddddddddddddmmmmmddhhysyhhhysyyyyyyyyyyyyyyyyyyyyyssooosysooosssssssssssssssyyhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhyhhyyso+++ooooooooooooo++++++++++ooooooooooooooooooooossyhhhyyysyhmmdddddddmdy+/++++/:---------------::::::::::://+oooo+o+/::::::::::::///////++++ooossyyyyyyyyysssyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyysssssssssssssss\n"
          "yyyyyyyyyyyyyyyyyyyyyyyyyys+//://+o+/:::/+sshhhhhddmdsosso//+//+osyhhhddddmmmmmmmmmmmmmmdhyysyhdmmhysysyyyyyyyyyyyyyyyyyyysssoosooosyhyyssssssssyyyyhhhhhhyyyyyhhhhhhhhhyyyyyyyyyyyyyyyyyyyyysooooooooooooo+++++/++++++++oooooooooooooooooooooossyhhhyyyysydmddddddddmms/:/++/:-----------------:::::::::++ooo+o++++/:::::::::::///////+++++oossyyyyyyyyyssssyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyssssssssssss\n"
          "yyyyyyyyyyyyyyyyyyyyyyyyyyo+///:/+oss+///oshhyyddmmmmhsso++++/+osyhhhhhhhddmmmdmdmmmmmmddhysoyhmmmdhsssyyyyyyyyyyyyyysyyyyyyyssooooyhhhyyyssssyyyyhhhyyyyysyyhhhhhhhhhyyyyyyyyyyyysssyssssooo++ooo+++++++/////++++++++oooooooossssoooooooooooossyhhhyyyyysymmdddddmmdmmy///++:------------------:::::::/+oooo++o++o+/::::::::::////////++++oosssyyyyyyyyyssssyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyysssssssss\n"
          "yyyyyyyyyyyyyyyyyyyysssyys//+o+//+osysosyydddhhdmmmmmmdhsooo++syhhhhhyyyhhddddddddddmddddhhsoshdmmmdssyyyssyysyyysyysssyyyhyyysooooshhdhhyyyyyyhhhhyosyyyyyhhhhhhhhhhyyyssssoooooooooooo+++++++++++///////////++++oooooooooossssssooooooooooossyhhhyyyyysyymmdddddmmdmmho+++/--------------------:::::/+oooo++ooooo+/:/:::::::////////++++ooossyyyyyyyyyssssyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyysssssssyy\n"
          "sssssssssssssssssssssssyyyo+oys+/+osyyyhhhddmddmmmmmmmdho++ooosyhhhdhyyyyyhhhhhhhhhhdhdddhyssyhmmmmmysyhyyysssssssssosyyhyyyyysoooosyhdddhhhhhhhysoo+++ossyhhhhhhyyssooo++++++ooo+++++//////////////////+++o+/oo++sssoooooosssssssoooooooooooshhhhhyyyyysyymmdddddmmddmdyo++:--------------------::::/+ooo++++oooooo+//::::::///////+++++ooosssyyyyyyyyyssssyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyy\n"
          "sssssssssssssssssssssssyyhyysyyooosyhhhhhdhdhshdmmdmmmmds++shdyssyyhhhhhyyyyhdddhhhhdddddyysoydmmmmmhsyhhhyysssssssoosyhhyyyyysooooosyyhhdhhhhys+++++++++osyhhysoo++++++ooo+++//::::::::::::::::://///++++oo+/oso+ooooooossssssssssoossoosoosyhdhhyyyysysyymmddddddmddmmhso+:-::------------------:::+ooooo+++oooooo+/::::::////////+++oooosssyyyyyyyyyysssyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyy\n"
          "sssssssssssssssssssssssyhysysyyhhddmmhssssoso:/sdmddddmddhhdmmmyossyyyyyhhhhhhhhhddddhhhhsssoydmmdmmhsyhhhhyysssssooosyyyyssyssooooooooossyhyso+++++++++++oooo+++++++++//:::------------:--:::///++oo++o++oo/++o+++ooooossssssssssooosssosssyhdhhyyyyyyysyymmmddddmmmmmmdys+/:::::::::::::---------::+ooooo+o+ooooooo+//://///////+++++oooosssyyyyyyyyyysssyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyy\n"
          "ssssssssssssssssssssssssssssyyyhhddddyssoo+oo:-/shdhddmmdmmdmmmds+shhyyyyyyhhhhhhdhhhhhhhsooshdddhdmdsyhhhhhyysssso+oyhysosssssooooooooooooooooooooooo+oo+++++///::--------------------::://+//+o+/++:/++/+o++++ooooooossssssssssssssssssosshddhyyyyyysysyydmmmddddmmmmmmhso/::::::::::::::::::::---:+oooo++o++ooooooo+/:////////++++++ooosssyyyyyyyyyyysssyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyy\n"
          "sssssssssssssssssssssssooosyyyyhhhyyysssoo+o+---:++:/shdmmmmmmmmdsoyyssssssssyyhyyyyyyyysooosdmmdhdmdyyhyyhhhyyssso+oyhyo+ossso++ooooooo++++++++++++////::::----------------::::-----:-::////+++o+/++//+++++++ooooooossossssssssssssssssssyhddhyyyyyyysyyyydmmmmmdmmmmmmmmyo//:::::::::::::::::::::::/osso++++o+ooooooo+/////////+++++ooosssyyyyyyyyyyyysssyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyy\n"
          "yyyyssssysyyssssysssssssosyyyyhddhyyyysso++o/---------/shdmmdmmmmy+oysssssssssyyyssyyyyysoosydmdhyhmdyyyyyhhddhysso+oyys+++++ooo++++++++/+/+++/:----------------::////////++////----::::/++++++//+++++++++++++ooooooosssssssssssssssssssssydhhyyyyyyyyyyyyyhmmmmmmmmmmmmNNdy+////////////:::::::::::::+oss+++oo+oooooooo+//////++++++oooosssyyyyyyyyyyyssssyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyy\n"
          "yyyyyyyyyyyyyyyyyyyyyssyyhhyyyhdhysssooosooo/-----------/oyyyyhhddsosysssssssyyyyyyyyyyysoosyyhhhhhdhyhhhhhdddhyyso+osys++++++++////////////+os+:------::://++++/+oo++++++//:--...--:///////+///+//++++++++oooooooooossssssssssssssssssosyhdhhyyyyyyyyyyyyyydmmmmmmmmmmmNNmho+//////+osso+/////:::::::/+yyo+++oooooooooooo++//++++++oooosssyyyyyyyyyyyysssyyhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhh\n"
          "yyyyyyyyyyyyyyyysysssooosyhdhhhdhysoso+++++s/::-:-----:--::::::/+soosysyyyyyyyhhhyyyyyhhhyyhhhhhhhhysyhddhhhhhhyyysoosyso+++++++/////////////+ys/-://++oooo++++///++////::-.....---::////://///////+++oossssssssssoooosssssssssssssssossyhdhyyyyyyyysssyyyyyhmmmmmmmmNmNNNNmho++++//+osso+/////////::::/oss++++++ooooooooooo++++++ooooossssyyyyyyyyyyyyssyhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhh\n"
          "yyyyyyyyyyysssyysyyssoooosyyyhdddysoso++++shdssyhs+/:::/oo+::://///+oyyyyyyyyyhhhyyhhhhhhddhhhhhhhhyyyhyyyyhhhhhhhsoossoo++++++++///+/////////sy+:+oooooooo+/+/:-::::-----.....----:::::////////++osyyyyyysssssooooo+oossssssssssssssosyhhhhyyyyyyyyssyyyyyyydmNNNNNNNNNNNNNmys+++++++++++++//////////::/osoo++++oooooooooosoo+++ooooossssyyyyyyyyyyyyyyyyhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhh\n"
          "yyyyyyyyyyyssssysssssooossyssyyhdhyssso+++yddmmmmdddddddmdy/::////++ossssssssssyyyyyyyyhhhddhhhhhhhyhhhyyyyyhhhhhysooosso+++++++++/+//////////oyo:+o+++/////::::--------------::-::::::::////+syyhhhhhhhhhyysoooo+++++oososssssssssssssyhhhyyyyyysyyyyyyyyyyyydmNNNNNNNNNNNMNmhsooooo+++++++++++//////////oyoo++ooooooooossssssoooooossssyyyyyyyyyyyyyyyyyhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhh\n"
          "yyyyyyyyyyyysssssssssooossysssyyhhyssoo+osdmdmmmmmmmmmmmmmdo////////oysssysoosssssssyhhhhhddhhhhhhyyhhhhyyyhhhyhhhyooossoo+o+++++++++/////////+ss//++//+////////-://::::::::::::::::::////+oyyyyyyyyyyyyyhhdhyo+++///+oossssssssssssssyhhhyyyyyysssyyyyyyyyyyyydmNNNNNNNNNNNNNmhysssooooooooo++++++++/////+yyso++oooooooosssssssssssssssyyyyyyyyyyyyyyyyyyhhhhhhhhhhhhhhhhhhhhhhyyyyyyyyyyhhhhhhhhhhyyyyyyyyyyyy\n"
          "yyyyyyyyyyyyyyyyyssssoooosyssssyhhhyso+osdmdmmmmmmmmmmmmmmmho///////oyyyyssoooosssssoyhhyyhdhhhhhhhhhhhhyyyyhhyhhysooossoooooo++++++++++//////+sy+:+//+//++//++/:-://///:::::///:::////+ossssssyyyyyyyyyyyhhddho///:/osssssssssssssssyhhhhyyyyyyyyyyyyyyyyyyyyyhdmNNNNNNNNNNNNNNmhyyyysssssoooooooo++++++/+syyyysooooosoosssssssyyyyyyyyyyyyyyhhhhhhhyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyy\n"
          "yyyyyyyyyyyyyyyyysssooooosyssssyyhdhsooydmmmmmmmmmmmmmmmmmmmhs+////sdmmmmmmmmmmmmmyydmmNmmmNNNNNmmNNNNmmmmmmmmmNmmmddmmmmdmmmmddddmmdddddddddddmmdhdyddddddddddhhhdddddddhddddddhhhhddddmmmmmmmddhhyyyyhmmmmNNNmdhhhddmmmmmmmmmmmmmmmmNNmmmmmmmmmmmmmddhyyyyyyyyhmNMMMMMMMMMMMMMMMMNmmdhyyysssssssoooooo+++oyyyyyssoooosssssssssyyyyyyhhhhhhhhhhhhhhhhyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyy\n"
          "yyyyyyyyyyyyyyyyyyysssooosysosssyhhhyhdmmmdmmdmmmmmmmmmmmmmmmdo//+/yMMmdddddddddMMNdMMmddddddddmMMMMmdddddddddhmMMMdddddddddddNMMMMdddhddddddddddmMMNMMmdddddddddddddhNMMMMmdddddddddddddddmmNMMMMNNmhyhMMNddddddddddddddddddNMMMNddddddddddddddmmNNMMMMMNdyyyhmMMMMMdyso+////+osydNMMMMNdyyyyyyyyssssssoooosyyyyyyssssssssssssyyyyyyhhhhhhhhhhhhhhhhyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyy\n"
          "yyyyyyyyyysyyyssyssssssssyyssssyyhhddmmmmmmmmmmmmmmmmmmmmmmmNmy+///hMM/`````````hMMNMM/````````:MMMMo``````````:MMM```````````yMMMM``````````````:MMMMN:``````````````yMMMMo``````````````````.-+yNMMNddMMy``````````````````yMMMy``````````````````.:odMMMNhdNMMNh/.`           ``./yNMMNhyyyyyyyyyyyyysssssyyyyyyyyyssssssssyyyyyyyhhhhhhhhhhhhhhhyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyy\n"
          "yyyyyyyyyyssyyyyyssooooosyyyyyyyhdddmmmmmmmmmmmmmmmmmmmmmmmmmmho//+hMM/         -NMMMM/        -MMMMo          -MMM`          yMMMM`             `mMMMN`              yMMMMs                     `.sNMMmMMs                  sMMMy                     `/dMMmMMMm:`                   .hMMmyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyhhhhhhhhhhhhhyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyy\n"
          "yyyyyyyyyyssyyysssooooooosssosyyyhdddmmmmmmdmddmmmmmmmmmmmmmmmho///yMM/          oMMMM/        -MMMMo          -MMM`          yMMMM`              yMMMh               yMMMMo                        /MMMMMs                  sMMMy                       .mMMMMN-                      .mMMyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyhhhhhhhhyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyy\n"
          "yyyyyyyyyysyyyysssooooooossoossyyhhdysoosyso++oshddmmmmmmmmmddy+//+hMM/          `dMMM/        -MMMMo          -MMM`          yMMMM`              /MMM+               yMMMMo          `//:`          yMMMMs                  sMMMy           /:.          +MMMMs          :dm+          sMMhyyyyyyyyyyyyyyyyyyyyyyyyyyyyyhhhhyyyyyyyyyyhyyyyyyyyyyyyyyyhyyyyyyyyyyyyyyyyyyyyyyyhyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyy\n"
          "yyyyyyyyyyssyyssssoooooosssssssyyhhhs/---:------:/osddhyssso++/////yMM/           -NMM/        -MMMMo          -MMM`          yMMMM`              .NMN-               yMMMMs          .MMNh          /MMMMs          `yyyyyyymMMMy          `MMm.         .MMMM/          dMMm          /MMhyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyhhhyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyy\n"
          "yyyyyyyyyyysssssyssooooosssssssyyhdho:------------::o+/::://://///+hMM/            oMM/        -MMMMo          -MMM`          yMMMM`               hMm`               yMMMMs          .MMMM`         .MMMMs          .MMmdddmmmMMy          `MMM-          NMMM:          dMMm          :MMhyyhyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyhyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyy\n"
          "yyyyyyyyyyyyyyysssysssssyysssyyyhhdh+:--------------::::::::://///+hMM/            `mM/        -MMMMo          -MMM`          yMMMM`               +Mh                yMMMMs          .MMMM`         .MMMMs          .MMhsysssyMMy          `MMM-          NMMM/          /NMNooooooooooyMMhyyyhyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyy\n"
          "yyyyyyyyyyyyyyysssooooosyyyyyyhhdddh/:------------:---::::/:////+++hMM/             :N/        -MMMMo          -MMM`          yMMMM`         `     .M+      .         yMMMMs          .MMMm`         :MMMMs          .MMNNNNNNNMMy          `MMN.         .NMMMy           .+dNMMMMMMNNNNmNhyhyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyy\n"
          "yyyyyyyyyysyyysssoooooosssssyyhhdddy/--------------::-::::://///+//hMM/              s/        -MMMMo          -MMM`          yMMMM`         :      d-     .:         yMMMMs          .yyo-         .dMMMMs          `yyyyyyyMMMMy          `ys/          +MMMMN:            `-+hNMMMNdhyyhyyyyhyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyhyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyy\n"
          "yyyyyyyyyyyyyssssoooooosssssyyhhddds:--------------::-:://////////+dMM/              `-        -MMMMo          -MMM`          yMMMM`         s      +      +:         yMMMMs                    `.:omMMMMMs                 `MMMMy                      `/NMMNMMm:              `-+dNMMNmhyhyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyy\n"
          "yyyyysyyyyyssssssoooooosssssyyhhddh+:-------------:/++sydhhyooo+++odMM/                        -MMMMo          -MMM`          yMMMM`        `d`     `      y:         yMMMMs                    ./ymMMMNMMs                 `MMMMy                   ./smMMMmyNMMNy:`              `:sNMMNdyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyy\n"
          "yyyyyyyyyyyyyyyyssooooossosyyyhdddy/------------:/ydmmmmmmmmmmmhoosmMM/                        -MMMMo          -MMM`          yMMMM`        `m:            N/         yMMMMs                       .+NMMMMs                 `MMMMy                    `-+dMMNyydNMMNdo-`              -yMMMhyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyy\n"
          "yyyyyyyyyyyyysssssssssyyyyyyhhhddds:-------------/shmmmmmmmmmmmyooymMM/        ..              -MMMMo          -MMM`          yMMMM`        `ms           -M/         yMMMMs          .hhs/          /MMMMs           ......-MMMMy           hy/         .yMMmhhdmNMMMNh+-`            `sMMmyyhyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyhhhhhhyyyyyy\n"
          "yyyyyyyyyyyyyssoooooosyyyyyyhhdddho:-----------:+oydmmmmmmmmmdsooyymMM/        -s              -MMMMo          -MMM`          yMMMM`        `md           +M/         yMMMMs          .MMMN`         `mMMMs          .mNNmmNmMMMMy          `MMN.         -MMMMMNNNNNNNNNmh+.           `mMMyyhyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyhhyhhhhhhhhyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyh\n"
          "yyyyyyyyyyyyysoooooooosssssyyyhddy+-----------/sddmmmmmmmmmdysosssymMM/        -N:             -MMMMo          -MMM`          yMMMM`        `mN.          hM/         yMMMMs          .MMMM`          yMMMs          .MMmmmmmmmMMy          `MMM-         `NMMMd----------sMNs`          sMMyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyhhh\n"
          "yyyyyyyyyyyyysooooooosysssssyhddhs/-----------/ydmmmmmmmdhyoosssssymMM/        -Md`            -MMMMo          -MMM`          yMMMM`        `NM/         `NM/         yMMMMs          .MMMM`          yMMMs          .MMmdmdmmmMMy          `MMM-          NMMMd          +MMMo          +MMyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyhhhh\n"
          "yyyyyyyyyyyyyysooooossysssssyhddyo:-----------:ohdddddhssoosssssyyymMM/        -MM+            -MMMMs          -MMM`          hMMMM`        `NMy         :MM/         yMMMMo          .MMMM`          yMMMs          .MMNNNNNNNMMy          `MMM-          NMMMd          +MMMd          /MMyyyyyyyyyyyyyyyyyyyyhhhhhhhhhhhhhhhyhhhhhhhhhhhhhhhhhhhhhyyyyyyhhhhhhhhhhhhhyhhhhhhhhhhhhhhhhhhhhhyyyyyyyyyyyyyhhhhh\n"
          "yyyyyyyyyyyyyyssssssyyyssssshhddy+:::-::::-:-::/ossooooossooooosssymMM/        -MMm.           -MMMMy          -MMN`         `dMMMM`        `NMm`        oMM+         yMMMMo          -MMMh           yMMMs          `hddhhddhNMMy          `MMM-          NMMMm`         /MMMd          +MMhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhyyyyysyyyyyyyhhhhh\n"
          "yyyhhhhhhhhhyysoossyyyyyyyyhdddhyo+o++++/+++ooooooooooossoooooosssydMM/        -MMMy           -MMMMm`         `hNs          .NMMMM`        `NMN-        dMM+         yMMMMo          `++:`           dMMMs                   yMMy          `MMM-          NMMMM-         .dNd:          yMMhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhyhyyyyyyssyyyyyyhhhhhh\n"
          "hhhhhhhhhhhhhyoooossyssssyyhdddhso+oo+oo+ooosso+ooooooosyoooosssssymMM/        -MMMM-          -MMMMMs                      `yMMMMM`        `MMM+       .NMM+         yMMMMo                         .NMMMs                   yMMy          `MMM-          NMMMMh`                      .NMNhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyhy\n"
          "hhhhhhhhhhyhhysoossyyysyyyhhddhyssssssoossssyssssssssssyyssssssssyymMM/        -MMMMd          -MMNMMMy.                   .hMMNNMM`        `MMMh       :MMM+         yMMMMs                        `hMMMMs                   yMMy          `MMM-          NMNMMMy.                    -dMMmhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyy\n"
          "yyyyyyyyyyyyyysssyyyyyyyhhhddhyysoosssooooosssssossssssyyyyyyyyhhhhmMM/        -MMMMM+         -MMdmMMMNs:``            `-sNMMNhNMM`        `MMMm.      sMMMo         yMMMMs                     `-omMMNMMs                   yMMy          `MMM-          NMddMMMNy:`              ./hNMMmhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhyyyyyyyyyyyyyyyyyyyyyyhhyyyyyyyyyyyyyyyy\n"
          "yyyyyyyyyyyyyyyhhhhhhhhhhdddddhyyyyyysoooooooooooosyhhhhhhhdhhhddddmMMdhhhhyhhhdMMmMMNhyyhhhhhhdMMdddNMMMMNdyo/::--:/+shmMMMNdyyNMMhhhhhhhyhhMMMMhhhhhhhNMMMmhhhhhhhhhmMMMMmyhhhhhhhhhhhhhhhhddmmNMMMMNmMMmhhhhhhhhhhhhhhhhyhyNMMNhhhhhhhyhhhMMMdhhhhhhhhyhMMdyhmNMMMNdso/::--:/+oydNMMMmdyhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhyyyyyyyyhhhhhhhhhhhhhhhhhhhhhhhh\n"
          "yyyyyyyyyyyyyyhddhhhhhdddddddddhhhhhysooooooooooosyhddhhhhddddddddddhhdddhddhhhhddydhddddhdhdmNNNmddddddmmNNMMMMMMMMMMMNNmdhyhyyddmmmdmmdmmmNNNmddhhhhhhhhhhhyhyyyyyyyyyyyyyhhhhhdddmmNNNNNNNMMMNMNNNNNNNMMNNMMNMMMMMMMMMNMNNMNMMNMMMMNNNNNMMNNNNNmmmmmmmmmmdhyyyhdmmNNMMMMMMMMMMMNNmddhhhhyhhyhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhh\n"
          "yyyyyyyyyyyyyhhdhhhhhddddddddddhhhhhyssossssssssyhdddddhhhddddddddhyossssssssssssyssysysoooooydmdddddddddhhhyyssoosyyssyyhhyyhyyyhyyhyyyyyhyddmdhysooooo+++++++++++oosssyyhhddmmmmmNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNmddhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhyhhhhhhhhhhhhhyhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhh\n"
          "yyyyyyyyyyyyhhddddddddddddmdddddhhhhyyssssssssyhdmdddddhhddddhddddhsossssssssssoossosooooooooydmddddddddhhyhssoooosysooyyyhhhhhyhhhhyhhhyhyyhhdmdhysosssyyhhhddmmmmNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNdhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhyhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhh\n"
          "yyyyyyyyyyyhhddhhhhhhhhhhdddddddNmmmmmmmmmmmmmmNNNNNNNNNNNNNNNNNNmNmdhmmmmdmmdddmdmdddddmdddmmNNNNNNNNNNNmNmmmddddmmmmmmmmmmmmmmmmdddhymmmmmmmNNNNNmmmmdNNNNNNMMMMMMMMMMMMMMMMMMMNNMMMMMMMMMMMMMMMMMNMNMMMMMMMMMMMNMMNMMMMMMMMMMMMNMMMNMMMMMMMMMMMNNmNNNNNNNNNmmNmNNmmmmmmmmmmmmmmmmmmmmmmmmmmmmmdhhhhhmmmNmmmmmmmmmmNNNNmmmmmmhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhh\n"
          "yyyyyyyyyyyhdddhhhhhhhhhhdddddddMMNddddddddddddddddddNNddddddddddddMMMMMNddddddddddddMMmddddddddddddddddddMMMMmdddddddddddddmmmNMMMMMMmNMMddddddddddNMMdMMMdddddddddddddddddddddNMMMMMdddddddddddmMMMMMNdddddddddddMMdddddddddddNMMMdddddddddddNMMMMdddddddddddddddddddMMMMNddddddddddddddmmNMMMMMMNdhdMMNdddhddddddddddddddmMNhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhh\n"
          "yyyyyyyyyyyhhdddhyyyyyyyhhdddddmMMs               `  yN. `  ``    `dMMMMs        `  :MM:                 `mMMM/           ```````./smMMMMMs`  `     +MMNMMm``    `  .. `        yMMMMN`          -NMMMMs          -MN           dMMM `         hMMMM                  -MMMMs  `     ``````````.:odMMMNdMMy  `               sMNhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhh\n"
          "yyyyyyyyyyyyyhhyysssssyyhhhdddddMMs                  sM/           yMMMM+           oMM:                  mMMM/                     `oNMMMN.        .MMMMMs         s/          oMMMMh           `NMMMM/          /MN           dMMM           hMMMM                  -MMMMs                     `/NMMNMMy                  oMNhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhh\n"
          "yyyyyyyyyyyyyyyyyssssssyhhhddddmMMs                  sMy           +MMMM:           hMM:                  mMMM/                       /NMMMy         dMMMM-        -Ms          /MMMM+            mMMMN.          sMN           dMMM           hMMMM                  -MMMMs                       -NMMMMy                  oMNhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhh\n"
          "yyyyyyyyyyyyssssyysssssyhhhdddddMMs                  sMm`          -MMMN.          `NMM:                  mMMM/          ./:`          hMMMM-        oMMMh`        hMd          -NMMM-            hMMMd           dMN           dMMM           hMMMM                  -MMMMs          `/:`          oMMMMy                  oMNhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhh\n"
          "yyyyyyyyyyyyyyyyhhyyyyyhhdddddhdMMs          `yyyyyyymMM:          `MMMm`          :MMM:          :yyyyyyyNMMM/          /MMy          +MMMMh        -MMM+        /MMN.         `NMMN`            sMMMs          .NMN           dMMM           hMMMM           +yyyyyyhMMMMo          .MMd`         -MMMMy          `yyyyyyymMNhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhyyyhhhhhhhyyhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhh\n"
          "yyyyyyyyyysssssyyyysssyyhhddhhhdMMs          .MMmmmmmNMMo           mMMd           oMMM:          +MMNNmmmNMMM/          /MMN          :MMMMM/        dMm`       `mMMM/          mMMh             +MMM/          :MMN           dMMM           hMMMM           hMNmmmmmmNMMo          .MMM.         `MMMMy          `MMNmmmmmmdhyyyyyyhhhhhhhhhhhhhhhyyyyyyyyyyyyyyyyyhhhhhyyyyyyyyyyyyyyyyyhhhhhhhhhhhhhhhhhhhh\n"
          "hhhyyyyyysssososyyysssyyyhddhhhdMMs          .MMdhhddmMMd`          yMMs           dMMM:          +MMddddddNMM/          /MMN          :MMNMMd`       oMs        sMMMMo          yMMo             :MMN.          oMMN           dMMM           hMMMM           hMmyyyyyydMMs          .MMM.         `MMMMy          `MMdyyyyyyyyyyyyyyyhhhhhhhhhhhhyyyyyyyyyyyyyyyyyyyyyyyyhhhhhhhhhhhhhhhhhhhhhhhyyyyyyhhhhhhhh\n"
          "yyyyyhyyysosooosyyssssyyhhdddhyhMMs          .MMNNNNNMMMN-          +MM+          `NMMM:          +MMNNNNNNMMM/          /MMm          /MMdMMM+       .m-       -NMMMMd          oMM:             .MMm           dMMN           ohhh           hMMMM           hMMNNNNNNNMMo          .MMN`         -MMMMy          `MMNNNNNNNdyyyyyhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhh\n"
          "yyyyyyhyyssoooosyysssssyhhdddhhhMMs          `yyyyyyhMMMM+          :MM:          :MMMM:          :yyyyyydMMMM/          -ys-         `hMMhmMMm.       /       `hMMhMMN.         /MM`              NMy          .NMMN                          hMMMM           oyyyyyymMMMMs          .ys:          sMMMMy          `yyyyyyyMMdhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhh\n"
          "yyyyyyyyysssssssyyyssyyyhddddhhdMMs                 `MMMMh`         `MN-          sMMMM:                 /MMMM/                     `.sMMNhhNMMo               /MMm+MMM:         -Mm               dM+          :MMMN                          hMMMM                  yMMMMs                      .+NMMMMy                  MMdhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhh\n"
          "yhyyyyyysoooooosssssssyyhdddhhhdMMs                 `MMMMN`         `mm`          dMMMM:                 /MMMM/                  `-+hmMMMdyydMMN-             `dMMs+dMMo         `Ny       .       yM:          oMMMN                          hMMMM                  yMMMMo                   ./ymMMMmMMy                  MMdhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhh\n"
          "yhyyyyyysoo+++oossoosssyhddhdddmMMs                 `MMMMM/          yd          .NMMMM:                 /MMMM/                   `.-oNMMmyyyNMMy             oMMdoohMMh          mo       s.      oN`          hMMMN                          hMMMM                  yMMMMo                    `-+mMMMMMy                  MMdhhhhhhhhhhhhhhhhhyyhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhh\n"
          "yyyyyyyysoo++ooossoossyyhdddddddMMs           ......-MMMMMy          oy          /MMMMM:          `......+MMMM/          :hy-         -mMMhyydMMN-           .NMNo+oyMMm`         h:       m+      /m          `mMMMN           -:::           hMMMM           `......hMMMMo          .hy/         .dMMMMy           .......MMdhhhhhhhhhhhhhhyyyyyyyhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhh\n"
          "yyhhyhyyso+++ooossoosshhddddhdddMMs          `NNmmmmmMMNMMm`         :o          sMMNMM:          /mNmmmmNNMMM/          /MMd          +MMhyyymMMh`          yMMy//+oNMM-         o.      .Md      .y          -NMMMN           dMMM           hMMMM           yNmmmmmNMMMMo          .MMN`         :MMMMy          `NmmmmmmMMdyhhhhhhhyhhhhhyyyyyyyhhhhhhhhhhhhhhhhhhyyhhhyyyyyyyhyyyyyyyyyyyyyyyyyyyyyyyyyyyyy\n"
          "yyhyyhhyysoo+oosssossyddddddhdddMMs          .MMmmmmmmmmMMM-         .:          dMMNMM:          +MMdddhhydMM/          /MMN          :MMyyyyhMMM.         `MMm/::/+mMM+         :`      +MN.      o          +MMMMN           dMMM           hMMMM           hMNhhhhhhmMMo          -MMM.         .MMMMy          `MMdhddhddhhhhhhhhhhyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyy\n"
          "yyyyyyyyyssssssyyysyhdddddddddddMMs          `MMmdddddmdNMMo          `         .NMNNMM:          +MMhhyysohMM/          /MMN          :MMhyyyyNMM.         `MMs::///hMMy         `       hMM+      -          yMMMMN           dMMM           hMMMM           hMmyyyyyydMMo          .MMM`         `MMMMy          `MMdyyyhyhhyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyy\n"
          "yyyyyyyyssooooosyssydddddddddddmMMs          .MMNNNNNNNNMMMd                    /MMmNMM:          +MMNNmmmmNMM/          /MMN          -MMhyyyyNMM.         `MMo:::/:oMMm`               `NMMh                `mMNNMN           dMMM           hMMMM           hMNmmmmmmNMMo          .MMM.         `MMMMy          `MMNNNmmNmmmyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyy\n"
          "yyyyyyyssoo+++ossooyddddddddddddMMs          `hhhhhhdhNMMMMM.                   sMMdmMM:          :hddhhhdhMMM/          /MMN          -MMhyyyyNMM.         `MMo:::::+NMN-               :MMMN.               -NMdNMN           dMMM           hMMMM           ohhhhhhhdMMMs          -MMM.         `MMMMy          `hdhhhddhNMNyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyy\n"
          "yyyyyyyssoo+++ossoosyhhdddddddddMMs                   yMNMMM+                  `dMNhmMM:                   NMM/          /MMN          -MMhyyyyNMM.         `MMo::////mMM+               oMMMM/               /MMyNMN           dMMM           hMMMM                   -MMMs          .MMM.         `MMMMy                   sMNyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyy\n"
          "yyyyyyysooooo+osssossyyhddddddddMMs                   yMNNMMh                  -NMmhmMM:                   NMM/          /MMN          -MMhyyyyNMM.         `MMo::////hMMy               dMMMMy               yMMsNMN           dMMM           hMMMM                   -MMMs          .MMM.         `MMMMy                   sMNyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyy\n"
          "yyyyyyyyysooooossssssyyhhdddddddMMs                   yMNmMMN`                 /MMdhmMM:                   NMM/          /MMN          -MMhyyyyNMM.         `MMo:::://sMMm`             .NMNMMm`             `dMNyNMN           dMMM           hMMMM                   :MMMo          -MMM.         `MMMMy                   sMNyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyy\n"
          "yyyyyyysssssssyhyyyhhhhyhhhdddddMMy  `                yMNdMMM:                 yMMhhmMM:                   NMM/          /MMN`         :MMhyyyymMM.         `MMo:::::/oMMM.  `          /MMyMMM:             .NMNhNMN           dMMM `    `  ` hMMMM`                  :MMMs        ` -MMM.         `MMMMy                 ` sMNyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyy\n"
          "yyyyyyysoo+++osyssshhhhyyyhddddhMMmhhhyhyyhhhhhyhhyhhyNMNdNMMmyhhhhhhhhhhhhyhyhNMNhhmMMdhhhhhhhhhhhhyhhhhhhMMMdhhhhhhhhhhdMMMyyhhhyhhhydMMhyyyyNMMhhyhhhhhyhhMMo::::::/mMMdyhyhhhhhhhhhhmMMomMMmhhhhhhhhhhyhyhMMmdMMMhhhhhhhhhhhNMMMhhhyhyhhyhyNMMMMhhhhhhhhhhhhhhyhhhydMMMmyhhhhhhhhhhMMMhhyhhhhyhhhMMMMmyhhyhhhhhhhhhhhhhhymMNyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyy\n"
          "yyyyyyysoooo+osssoshhhhyyyyhhddddhhhdmmmmmmmdhyhhmmmmmmNmdmmmmdmmmmmmmmmmdmmNNNmmmhhdmmmmmmmmNNNNNmmmdhhhhhhhhdddddddmmmmddddddddddddmddddyyyyydmddddmdddddhyyy/:::::::syyyyyhhhhhhhhddddddoyhhhhhhhhddddddddddNmmmdhhyyyyyyysyyyysyyyyyyyyyyyhyyhhhhhhhhhhhhdddmddddmmmmmddmddmmddmmdddmdddmmdddmddddmddmmdmmmmmmmmmmmmmmmdmmmdyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyy\n"
          "hyyyyyssoooooosssosyhhhyyyhhhhhhy+/+syyhhhhhs++oyhddddddddddhyyyyyyyyyyyyhhhmmmmdddhhhhhhhhddddmmddhhsoooooooossssssyyyhhyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyy+::::::::::////////+++++ooosssyyssoooooooosssssssyyhdmNdy+/::::-:---:::::::////////////+++++++++++syyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyy\n"
          "hhhhysoooo+++osssosyhhhyyhhhyyhhhys++osyyysso++oydddddddddddhyyyyyyyyyyyyyyhdmmddddhhhhhhhhdddmmmmdhhssooo++++syysssyyhhhyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyy+:::::::::://///////++++ooosssyyyysssosssssssssssyyhdmNmy+/::---:---::::::::///////////+++++++++++syyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyhhdoohhhyyhyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyy\n")


def disp_errors_dict(err):
    dictionary = {
        'unx': f'Polynomial expression probably false\n\n'
               f'Unexpected \x1b[1;37;41m {err[1]} \x1b[0m\n\n',
        'sign': f'Polynomial expression probably false\n\n'
                f'\x1b[1;37;41m {err[1]} \x1b[0m\n\n is missing before an expression\n\n',
        'n_equal': f'Polynomial expression probably false\n\n'
                   f'Unexpected number of \x1b[1;37;41m {err[1]} \x1b[0m\n\n',
        'deg>2': f'Polynomial degree \x1b[1;37;41m {err[1]} \x1b[0m is strictly greater than 2, can\'t solve\n\n',
        'pow_odr': f'Polynomial expression probably false\n\n'
                   f'Power \x1b[1;37;41m {err[1]} \x1b[0m is missing\n\n'}

    print(f'\n{dictionary[err[0]]}')


def check_wrong_pattern(pattern, test_):
    for wrong in pattern:
        for n, pat in enumerate(wrong):
            if pat:
                return 'unx', pat

    if test_:
        return 'unx', test_


def parsing(pattern):
    err_key = ''
    err = []
    equal_nbr = 0
    for e, exp in enumerate(pattern):
        if exp[EQUAL] == '=':
            equal_nbr += 1
        else:
            if not exp[SIGN] and e != 0:
                err_key = 'sign'
                err = '+ or -'

    if not equal_nbr or equal_nbr > 1:
        err_key = 'n_equal'
        err = '='

    return err_key, err


def formatting(g_pattern):
    equal = 0
    formatted_pattern = []

    for p in g_pattern:
        p = list(p)
        p[NUMBER] = round(float(p[NUMBER]), 1)
        p[POWER] = int(p[POWER])
        if p[EQUAL] == '=':
            equal = 1
        if equal:
            p[EQUAL] = ''
            if p[SIGN] != '-':
                p[SIGN] = '-'
            else:
                p[SIGN] = ''
        if p[SIGN] == '-':
            p[NUMBER] = -(p[NUMBER])
        p[SIGN] = ''
        formatted_pattern.append(p)

    return formatted_pattern


def reducing_form(g_pattern):
    pattern = formatting(g_pattern)

    logger.debug(f'\n/*/-------\nPrepared pattern to simplify {pattern}\n/*/-------\n')

    for e_1, p_1 in enumerate(pattern):
        if p_1[NUMBER] == 0:
            pattern.pop(e_1)
        else:
            for e_2, p_2 in enumerate(pattern):
                if e_1 != e_2:
                    if p_1[POWER] == p_2[POWER]:
                        p_1[NUMBER] = p_1[NUMBER] + p_2[NUMBER]
                        pattern.pop(e_2)

    pattern.sort(key=lambda x: x[POWER])

    logger.debug(f'\n/*/-------\nReduced pattern {pattern}\n/*/-------\n')

    res_str = ''
    res_lst = []
    for n, r in enumerate(pattern):
        if r[NUMBER] != 0:
            res_str += f' {"+" if r[NUMBER] > 0 and n != 0 else ""}' \
                       f' {int(r[NUMBER]) if r[NUMBER].is_integer() else r[NUMBER]} * X^{r[POWER]}'
            res_lst.append(r)

    if not res_str:
        return INF, res_lst

    print(f'Polynomial degree = {res_lst[-1][POWER]}')

    if res_lst[-1][POWER] > 2:
        return ERROR, 'deg', res_lst[-1][POWER]

    pow_ = 0
    for exp in pattern:
        if exp[POWER] > pow_:
            return ERROR, 'pow', pow_
        else:
            pow_ += 1

    print(f'Reduced form:{res_str} = 0')

    return OK, pattern


def gcd(a, b):
    """
    Greater Common Divisor
    :param a: Int
    :param b: Int
    :return: Int
    """
    while b:
        a, b = b, a % b
    return a


def discriminant_calc(reduced):
    exp_0 = reduced[0]
    if reduced[-1][POWER] == 2 and not reduced[-1][NUMBER]:
        reduced.__delitem__(2)
    if reduced[-1][POWER] == 1 and not reduced[-1][NUMBER]:
        reduced.__delitem__(1)

    if reduced[-1][POWER] == 0:
        print(f'\n\x1b[4;33mNo solution, I swear I did my best here... ¯\_(ツ)_/¯ \x1b[0m \n')
    elif reduced[-1][POWER] == 1:
        exp_1 = reduced[1]
        number = 0
        num = 0
        if exp_0[NUMBER] == 0:
            num = 1
        elif (exp_0[NUMBER] / exp_1[NUMBER]).is_integer():
            num = 1
            number = int(-exp_0[NUMBER] / exp_1[NUMBER])
        else:
            logger.debug(f'\n/*/-------\nTrying to make Egyptian fraction with {exp_0[NUMBER]}'
                         f' and {exp_1[NUMBER]}\n/*/-------\n')
            num_1 = -int(round(exp_0[NUMBER], 1) * 10)
            num_2 = int(round(exp_1[NUMBER], 1) * 10)

            res_gcd = gcd(num_1, num_2)
            logger.debug(f'\n/*/-------\nEuclidean algorithm with GDC {res_gcd}\n/*/-------\n')
            num_1 = int(num_1 / res_gcd)
            num_2 = int(num_2 / res_gcd)

        print(f'\nResult is \x1b[1;30;42m {number if num else f"{num_1} / {num_2}"} \x1b[0m\n')

    elif reduced[-1][POWER] == 2:
        exp_1 = reduced[1]
        exp_2 = reduced[2]

        delta = (exp_1[NUMBER] * exp_1[NUMBER]) - (exp_0[NUMBER] * exp_2[NUMBER] * 4)
        logger.debug(f'\n/*/-------\nDiscriminant = {int(delta) if delta.is_integer() else delta}\n/*/-------\n')
        if delta > 0:
            print(f'Discriminant is strictly positive, the two solutions are:\n'
                  f'\x1b[1;30;42m({int(-exp_1[NUMBER]) if exp_1[NUMBER].is_integer() else exp_1[NUMBER]}'
                  f' - √{delta: .2f}) / '
                  f'{int(exp_2[NUMBER] * 2) if (exp_2[NUMBER] * 2).is_integer() else exp_1[NUMBER]} \x1b[0m\n\n'
                  f'\x1b[1;30;42m({int(-exp_1[NUMBER]) if exp_1[NUMBER].is_integer() else exp_1[NUMBER]}'
                  f' + √{delta: .2f}) / '
                  f'{int(exp_2[NUMBER] * 2) if (exp_2[NUMBER] * 2).is_integer() else exp_1[NUMBER]} \x1b[0m\n\n')
        elif delta < 0:
            print(f'Discriminant is strictly negative, the two solutions are:\n'
                  f'\x1b[1;30;42m({int(-exp_1[NUMBER]) if exp_1[NUMBER].is_integer() else exp_1[NUMBER]}'
                  f' - i * √{delta: .2f}) / '
                  f'{int(exp_2[NUMBER] * 2) if (exp_2[NUMBER] * 2).is_integer() else exp_1[NUMBER]} \x1b[0m\n\n'
                  f'\x1b[1;30;42m({int(-exp_1[NUMBER]) if exp_1[NUMBER].is_integer() else exp_1[NUMBER]}'
                  f' + i * √{delta: .2f}) / '
                  f'{int(exp_2[NUMBER] * 2) if (exp_2[NUMBER] * 2).is_integer() else exp_1[NUMBER]} \x1b[0m\n\n')
        else:
            print(f'Discriminant is zero, the only solution is \x1b[1;30;42m '
                  f'{-exp_1[NUMBER] / (exp_2[NUMBER] * 2)} \x1b[0m\n')
        pass


if __name__ == '__main__':
    parser = argparse.ArgumentParser(prog='py ComputorV1.py')
    parser.add_argument('-d', '--details', action='store_true', help='Detailed computation', default=False)
    args = parser.parse_args()
    logger = logging.getLogger()
    if args.details:
        logger.setLevel(logging.DEBUG)
    else:
        logger.setLevel(logging.INFO)

    stream_handler = logging.StreamHandler()
    stream_handler.setLevel(logging.DEBUG)
    logger.addHandler(stream_handler)
    logger.debug('\n/*/-------\n Detailed mode activated \n/*/-------\n')

    while True:
        try:
            in_put = input('\x1b[5;30;47mPlease enter your polynomial expression :\x1b[0m ')
        except KeyboardInterrupt:
            sys.exit(print('\nYou\'ll pay for that !'))

        error = ['', '']

        if in_put.upper() == 'EXIT' or in_put.upper() == 'EXIT()':
            sys.exit(print('\nYou\'ll pay for that !'))

        in_put = re.sub(r'''(^\s*[\"\']|[\"\']\s*$)''', '', in_put, re.VERBOSE)

        global_pattern = re.findall(r'''
                                      (\=)?\s*                     # Equal if there's one
                                      ([\+\-])?\s*                 # Sign if there's one
                                      (\d+\.\d+|\d+)               # One or more number(s) (float or not) = variables
                                      \s*\*\s*[xX]\s*[\^]\s*       # spaces '*' spaces 'x' or 'X' spaces '^' spaces
                                      (\d+\.\d+|\d+)               # One or more number(s) (float or not) = coefficients
                                    ''', in_put, re.VERBOSE)

        wrong_pattern = re.findall(r'''
                                       ([^0-9\+\-\=\. *^xX])         # Catch wrong char
                                       |
                                       ([\-]\s*[^\d ]\s*)            # Delimit the usage of '-' (only figures)
                                       |
                                       ([\+]\s*[^\d xX]\s*)          # Delimit the usage of '+' (figures and xX)
                                       |
                                       ([\=]\s*[^\d \+\-xX]\s*)      # Delimit the usage of '=' (figures, xX, signs)
                                       |
                                       ([\*]\s*[^\d \+\-xX]\s*)      # Delimit the usage of '*' (figures, xX, signs)
                                       |
                                       ([xX]\s*[^\^ \+\-\=]\s*)      # Delimit the usage of 'xX' (pow, signs, equal)
                                       |
                                       ([\^]\s*(\d\s*\.|[^ \d])\s*)  # Delimit the usage of '^' (only int)
                                       |
                                       ([\.][^\d])                   # Delimit the usage of '.' (catches '..')
                                       |
                                       (\d*\.\d+\.\d+)               # Delimit the usage of '.' (catches '1.1.1')
                                    ''', in_put, re.VERBOSE)

        test = in_put.replace(' ', '')

        for pat in global_pattern:
            for p in pat:
                if p in test:
                    test = test.replace(p, '', 1)
            test = test.replace('*X^', '', 1)

        if wrong_pattern or test:
            error = check_wrong_pattern(wrong_pattern, test)

        elif global_pattern:
            logger.debug(f'\n/*/-------\nPattern catched {global_pattern}\n/*/-------\n')
            error = parsing(global_pattern)
            if not error[0]:
                reduced_form = reducing_form(global_pattern)
                if reduced_form[0] == ERROR:
                    if reduced_form[1] == 'deg':
                        error = ('deg>2', reduced_form[2])
                    elif reduced_form[1] == 'pow':
                        error = ('pow_odr', reduced_form[2])
                    else:
                        error = ('unx', '')
                elif reduced_form[0] == OK:
                    discriminant_calc(reduced_form[1])
                else:
                    dumb_func()

        else:
            print(f'It\'s like it\'s not working between you and me...\n\n'
                  f'"{in_put}"\n\n'
                  f'Really ?\n')

        if error[0]:
            disp_errors_dict(error)
