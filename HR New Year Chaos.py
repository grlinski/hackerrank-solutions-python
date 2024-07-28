

# HR New Year Chaos
# https://www.hackerrank.com/challenges/new-year-chaos/problem?h_l=interview&playlist_slugs%5B%5D=interview-preparation-kit&playlist_slugs%5B%5D=arrays


"""

Explanation
Queue from 1 onwards
Can bribe the person in front of you to swap positions
If they swap they still wear the same number
One person can only bribe twice max.

I will get a list.
Find out how many bribes it took to reach this state, or if it is even possible
All lines start normally from 1 onwards
Ex
3 1 2
To get to this state it took 3 bribes.



"""
"""
General thoughs.
A number can only move ahead 2 spaces.
However a number can move backwards any amount of times

So there needs to be a check to make sure nothing is more than 2 spots ahead of where it started.



Potentially, Do What I Did for Minimum Swaps
Have two dictionaries, one with the sequence numbers and their position
And another with the positions and the sequence number.
Try and work backwards to an ordered sequence.

1
5
2 1 5 3 4

So Swaps, Work from the back and push to the back.
2 1 5 3 4
2 1 3 5 4
2 1 3 4 5
1 2 3 4 5


Doesn't work going front to back
Also make sure a number is not at a position 2 less than it should be.
For example if 5 is at position 2, then this config is chaotic.
This really is just like Minimum swaps except for the following.
Work back to front.
Count how many steps a number moves backwards.
If a number is at a position 2 less than itself then the seq is chaotic.
A number can though be greater by any amount than its position.
Reminder that closer to 1 is a higher position.







"""


def minimumBribes(q):
    # Seq: Pos
    dx = {}
    # Pos: Seq
    dr = {}
    for i in range(0, len(q)):
        dx[q[i]] = i + 1
        dr[i + 1] = q[i]


    total = 0
    for i in range(len(q)-1,0,-1):


        if dr[i] > dr[i+1]:
            #print('pos',i)
            #print('before',dr)
            #print(dr[i],dr[i+1],i)
            h1 = dr[i]
            h2 = dr[i + 1]
            dr[i + 1] = h1
            dr[i] = h2
            total+=1
            #print('after', dr)
            print('Swap', dr[i],'with',dr[i+1])

            # So that All Works
            # Now check if the moved value is still larger than the next one.


            if i+2 > len(q):
                pass
            elif dr[i+1] > dr[i + 2]:
                h1 = dr[i+1]
                h2 = dr[i + 2]
                dr[i + 2] = h1
                dr[i+1] = h2
                total += 1

                # Last Check, if the number is still greater than the seq is too chaotic.
                # Note this will screw up if we are checking at the end.
                if i + 3 > len(q):
                    pass
                elif dr[i + 2] > dr[i + 3]:
                    return 'Too chaotic'



    return total



cases = int(input())

for i in range(cases):
    n = int(input())
    q = list(map(int, input().strip().split(' ')))




    print(minimumBribes(q))





























"""

Test Case

1
1000
3 1 5 4 2 8 6 10 11 9 13 7 15 12 17 18 19 20 16 14 23 21 25 24 27 26 22 30 31 29 28 34 33 32 37 35 39 40 41 38 36 44 45 46 43 42 49 48 47 52 53 50 55 54 51 58 59 60 57 56 63 64 61 66 65 68 69 67 62 72 71 74 70 76 75 73 79 78 81 82 77 84 83 86 80 88 87 85 91 90 89 94 92 96 95 93 99 98 101 100 103 97 105 104 102 108 109 110 106 112 111 114 115 113 107 118 117 116 121 122 120 119 125 124 123 128 127 126 131 129 133 134 132 136 130 138 137 135 141 139 143 144 142 140 147 145 149 148 146 152 151 154 153 150 157 158 159 156 155 162 163 164 160 166 167 165 161 170 171 169 173 172 168 176 175 174 179 178 181 182 180 177 185 184 183 188 187 186 191 192 190 189 195 196 194 193 199 197 201 200 198 204 203 206 207 208 205 202 211 210 213 212 209 216 215 214 219 218 217 222 221 224 223 220 227 226 225 230 231 229 233 234 235 232 228 238 236 240 241 242 239 237 245 246 244 243 249 250 248 247 253 254 252 256 251 258 255 260 261 259 257 264 263 266 267 262 269 265 271 272 273 270 268 276 275 278 274 280 279 277 283 282 281 286 287 284 289 288 285 292 293 291 295 294 290 298 296 300 299 297 303 302 301 306 305 304 309 307 311 312 310 308 315 314 313 318 316 320 321 317 323 319 325 326 324 322 329 327 331 332 330 334 333 328 337 336 335 340 338 342 341 344 343 339 347 345 349 350 348 346 353 352 351 356 355 358 359 357 361 354 363 362 360 366 365 364 369 368 367 372 370 374 371 376 373 378 379 377 375 382 380 384 385 383 381 388 389 390 386 392 387 394 393 391 397 398 399 396 395 402 403 404 401 400 407 405 409 406 411 412 410 414 408 416 415 413 419 420 421 418 423 417 425 426 422 428 424 430 431 429 433 432 427 436 435 434 439 440 437 442 438 444 441 446 445 443 449 447 451 448 453 452 450 456 457 454 459 455 461 458 463 460 465 464 462 468 467 470 469 472 471 466 475 473 477 476 479 478 474 482 481 484 480 486 483 488 485 490 487 492 489 494 493 491 497 496 499 498 495 502 500 504 501 506 505 503 509 508 511 507 513 510 515 516 517 512 519 514 521 520 518 524 525 523 522 528 526 530 531 529 527 534 533 536 535 532 539 540 538 537 543 544 541 546 542 548 547 550 551 549 545 554 553 556 552 558 559 557 555 562 561 564 560 566 567 565 569 568 563 572 573 570 575 571 577 576 574 580 581 579 578 584 583 582 587 585 589 586 591 590 593 592 588 596 597 595 594 600 599 602 598 604 601 606 605 603 609 608 607 612 613 614 615 611 610 618 617 616 621 619 623 624 625 622 627 626 629 628 620 632 631 630 635 634 637 636 633 640 639 642 638 644 641 646 647 645 643 650 651 652 653 649 648 656 657 655 654 660 661 659 663 658 665 662 667 666 664 670 669 668 673 671 675 674 677 678 676 672 681 680 679 684 682 686 687 685 689 688 683 692 693 691 695 696 697 690 699 700 698 694 703 701 705 704 702 708 707 706 711 712 710 709 715 713 717 714 719 718 716 722 723 721 720 726 725 724 729 730 728 732 727 734 731 736 733 738 735 740 739 737 743 742 741 746 747 745 744 750 751 749 748 754 755 753 752 758 759 757 761 762 760 756 765 764 763 768 769 767 766 772 773 774 771 770 777 778 776 775 781 779 783 780 785 782 787 786 789 788 784 792 790 794 791 796 795 798 797 793 801 800 799 804 803 806 805 802 809 810 808 807 813 814 812 811 817 815 819 820 821 818 816 824 825 823 827 822 829 828 826 832 833 830 835 834 831 838 837 836 841 840 843 844 842 839 847 845 849 848 851 850 846 854 853 852 857 856 859 858 855 862 861 864 860 866 863 868 869 867 865 872 870 874 875 871 877 878 876 880 873 882 881 879 885 884 887 886 883 890 891 889 888 894 895 892 897 898 896 893 901 900 903 902 899 906 905 908 907 904 911 909 913 910 915 916 914 912 919 917 921 918 923 920 925 924 922 928 929 927 931 926 933 934 932 930 937 936 935 940 941 939 938 944 945 946 943 942 949 948 947 952 951 950 955 953 957 956 954 960 961 959 958 964 965 962 967 968 966 963 971 970 973 974 969 976 972 978 977 980 981 979 975 984 982 986 987 983 989 988 985 992 991 990 995 996 993 998 997 1000 999 994


Expected
1201

Mine
951



"""
























# Unused Code
"""
def minimumBribes(q):
    total = 0
    for i in range(0,len(q)):
        # Current Value, and Position. Position just makes my life easier
        c = q[i]
        p = i+1
        # So AFAIK the too chaotic check works.
        if c-p >2:
            return 'Too chaotic'
        # How to correctly calculate bribes?
        else:
            try:
                c2 = q[i+1]
                if c > c2:
                    total+=1
            except:
                pass
            try:
                c3 = q[i+2]
                if c > c3:
                    total += 1
            except:
                pass

    return total//2
"""


"""
def minimumBribes(q):
    total = 0
    for i in range(len(q)-1,-1,-1):
        # Current Value, and Position. Position just makes my life easier
        c = q[i]
        p = i+1
        # So AFAIK the too chaotic check works.
        if c-p >2:
            return 'Too chaotic'
        # How to correctly calculate bribes?
        else:
            try:
                c2 = q[i-1]
                if c < c2:
                    total+=1
            except:
                pass
            try:
                c3 = q[i-2]
                if c < c3:
                    total += 12
            except:
                pass

    return total//2



"""








