from data import markers, years
from data import ra_cyrus, dec_cyrus, ra_muslim, dec_muslim, ra_ald, dec_ald, ra_ple, dec_ple
from utils import wrap180

#-559: Kingdom of Cyrus the Great
#636: Muslim invasion
RA_cyrus, DEC_cyrus = wrap180(ra_cyrus, dec_cyrus)
RA_muslim, DEC_muslim = wrap180(ra_muslim, dec_muslim)
RA_aldeb, DEC_aldeb = wrap180(ra_ald, dec_ald)
RA_ple, DEC_ple = wrap180(ra_ple-0.25, dec_ple)


#ann = [*zip(RA,DEC)]

def add_annotation(ax, ann):
    for i in range(len(ann)):
        label = years[i]
        ax.annotate(label,
                     (ann[i][0], ann[i][1]),
                     textcoords="offset points",
                     xytext=(0,5),
                     ha='center')
        ax.annotate('Aldebaran',
                    xy=(RA_aldeb, DEC_aldeb),
                    xytext=wrap180(67,12),
                    arrowprops=dict(arrowstyle='->', color='g', shrinkB=3, lw=2),
                    ha='center', va='center',
                    bbox=dict(boxstyle='round,pad=0.2', fc='white', alpha=0.3),
                    )
        ax.annotate('Pleiades',
                    xy=(RA_ple, DEC_ple),
                    xytext=wrap180(50,27),
                    arrowprops=dict(arrowstyle='->', color='g', shrinkB=3, lw=2),
                    ha='center', va='center',
                    bbox=dict(boxstyle='round,pad=0.2', fc='white', alpha=0.3),
                    )

        ax.annotate('Elamite Kingdom\nInvention of writing',
                    xy=wrap180(*markers[1][:2]),
                    xytext=wrap180(67,33),
                    arrowprops=dict(facecolor='black', shrink=0.2),
                    horizontalalignment='center',
                    verticalalignment='center',
                    bbox=dict(boxstyle='round,pad=0.2', fc='yellow', alpha=0.3),
                    )
        ax.annotate('Kingdom of\nCyrus the Great',
                    xy=(RA_cyrus, DEC_cyrus),
                    xytext=wrap180(40,-5),
                    arrowprops=dict(facecolor='black', shrink=0.05),
                    horizontalalignment='left',
                    verticalalignment='bottom',
                    bbox=dict(boxstyle='round,pad=0.2', fc='yellow', alpha=0.3),
                    )
        ax.annotate('Muslim invasion',
                    xy=(RA_muslim, DEC_muslim),
                    xytext=wrap180(17.5,-5),
                    arrowprops=dict(facecolor='black', shrink=0.05),
                    horizontalalignment='center',
                    verticalalignment='center',
                    bbox=dict(boxstyle='round,pad=0.2', fc='yellow', alpha=0.3),
                    )
    return ax

