import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# create a sample DataFrame
df = pd.read_excel("bad_laws.xlsx")
df=df.rename(columns={'Supreme Court October Term':'Date',
                     'Author(s) of Main Opinion':'Authors',
                     'Subject Matter(s)':'Subject Matter',
                     'Federal or State Provision(s)?':'Provisions',
                     'Description of Unconstitutional Provision(s)':'Description',
                     'Constitutional Provision(s) Invoked':'Constitutional Provisions Invoked'})
dates=pd.read_excel('bad_laws.xlsx',sheet_name='Sheet2')
# create a sample dictionary
word_dict = {'U.S.C.': 'Fed','Alabama':'AL','Alaska':'AK','Arizona':'AZ','Arkansas':'AR','California':'CA','Colorado':'CO','Connecticut':'CT','Delaware':'DE','Florida':'FL','Georgia':'GA','Hawaii':'HI','Idaho':'ID','Illinois':'IL','Indiana':'IN','Iowa':'IA','Kansas':'KS','Kentucky':'KY','Louisiana':'LA','Maine':'ME','Maryland':'MD','Massachusetts':'MA','Michigan':'MI','Minnesota':'MN','Mississippi':'MS','Missouri':'MO','Montana':'MT','Nebraska':'NE','Nevada':'NV','New Hampshire':'NH','New Jersey':'NJ','New Mexico':'NM','New York':'NY','North Carolina':'NC','North Dakota':'ND','Ohio':'OH','Oklahoma':'OK','Oregon':'OR','Pennsylvania':'PA','Rhode Island':'RI','South Carolina':'SC','South Dakota':'SD','Tennessee':'TN','Texas':'TX','Utah':'UT','Vermont':'VT','Virginia':'VA','Washington':'WA','West Virginia':'WV','Wisconsin':'WI','Wyoming':'WY','D.C.':'DC','Chicago':'IL','Los Angeles':'CA','Pub. L.':'Fed','Omnibus':'Fed','positive for cocaine':'SC','School policy opening school to public use, but prohibiting use of school for religious purposes.':'NY','Mo.':'MO','P.R.':'PR','Fla.':'FL','Atlanta':'GA','St. Paul':'MN','Virgin Islands':'VI','District of Columbia':'DC','C.F.R.':'Fed','La.':'LA','New Orleans':'LA','A bylaw of a university board of curators that prohibited distribution of materials containing':'MO','Rockford':'IL','N.C.':'NC','Cincinnati':'OH','Birmingham':'AL','Ala.':'AL','Provision of the Violence Against Women Act creating a federal civil remedy for victims of gender-motivated violence.':'Fed','School district policy that allowed students to initiate and lead prayer before home football games.':'TN','N.Y.':'NY','P. R.':'PR','Ga.':'GA','Subversive Activities Control Act':'Fed','Dallas':'TX','Ill.':'IL','Cal.':'CA','Ca.':'CA','Tex.':'TX','Prince Edward':'VA','Immigration and Nationality':'Fed','Greenville':'SC','L.A.':'CA','Baxley':'NY','Wis.':'WI','Okl.':'OK','Urgent Deficiency Appropriation':'Fed','Ark.':'AK','Conn.':'CT','N.M.':'NM','Tenn.':'TN','Ky.':'KY','Minn.':'MN','Pa.':'PA','Wash.':'WA','Okla.':'OK','Mass.':'MA','Act of February':'Fed','Act of January':'Fed','Act of March':'Fed','Act of June':'Fed','Act of May':'Fed','Act of July':'Fed','Act of April':'Fed','Act of August':'Fed','Act of September':'Fed','Act of December':'Fed','Act of October':'Fed','Act of Noveber':'Fed','Miss.':'MS','N.J.':'NJ','Morristown':'NJ','Kan.':'KS','Neb.':'NE','W. Va.':'WV','Houston':'TX','Detroit':'MI','Denver':'CO','St. Louis':'MO','Minn':'MN',
             'November 1940':'MI',
             'Revenue Act of 1924':'AL',
             'Loan Act of 1933':'WI',
             'Tenure of Office':'Fed',
             'Future of Trading Act':'Fed',
             'Chinese Bookkeeping':'Fed',
             'Act of Congress June':'Fed',
             'S.C.':'SC',
             'Fl':'FL',
             'Provisions imposing a federal tax':'Fed',
             'federal tax':'Fed',
             'Ariz':'AZ',
             'Agricultural Adjustment Act':'Fed',
             'Bituminous':'Fed',
             'National Prohibition Act':'Fed',
             '1933 Economy Act':'Fed',
             'Seattle':'WA',
             'Banking Act of 1919':'GA',
             'Future Trading Act':'Fed',
             'Stark County':'OH',
             'Municipal ordinance requiring':'VA',
             'North College Hill':'OH',
             'License fee or excise of a given per cent':'MA',
             'The due process requirements of notice and hearing':'CO',
             'Ordinance according to a consolidated municipal':'OH',
             'Ordinance reducing the rate of fares':'OH',
             'City ordinances that adjusted the rate of fare':'MI',
             'Ordinance expanding city limites beyond':'CA',
             'A municipal ordinance granting to a':'LA',
             'A state connot validly sell for taxes lands':'TN',
             'State laws that deprived local government of power to levy tax necessary to pay bond obligations':'Fed',
             'A statute increasing a tax above the rate stipulated in the stat':'NJ',
             'A city ordinance that levied a tax on stock issued by the United States impaired the federal borrowing power and was void (Art. VI).':'WV',             
             'When a utility is chartered with an exclusive privilege of supplyinga city with water, a subsequently enacted ordinance authorizingan individual to supply water to a hotel impaired the obligation of contract.':'LA',
             'A state cannot validly sell for taxes lands that the United States owned at the time the taxes were levied, but in which it ceased to have an interest at the time of sale':'TN',
             'A state rate-regulatory law that empowered a commission to establish rate schedules that were final and not subject to judicial review as to their reasonableness violated the Due Process and Equal Protection Clauses of the Fourteenth Amendment':'IL',
             'Ordinance expanding city limits beyond those to be served by autility leasing a municipalityâ€™s water works and effecting diminutionof the rates stipulated in the original agreement without any equivalentcompensation impaired the obligation of contract between the utilityand the city.':'CA',
             'Municipal contract with utility fixing the maximum rate to be chargedfor supplying water to inhabitants was invalidly impaired by subsequentordinances altering said rates.':'MS',
             'N/A':'CA'}


def replace_words(text, word_dict):
    for key, value in word_dict.items():
        if key in text:
            return value
    return ''
#------------------------------------------------------------------------------

df['State'] = df['Description'].apply(lambda x: replace_words(x, word_dict))
df_nofed=df[~df['State'].str.contains('Fed')]
dates['abbrv']=dates['state'].apply(lambda x: replace_words(x, word_dict))
dates=dates.rename(columns={'state':'State Name','date of admission':'Date','abbrv':'State'})
dates['Exist Time']=2023-dates['Date']
counts=df['State'].value_counts().sort_values()
counts=counts.reset_index(drop=False)
counts=counts.rename(columns={'index':'State','State':'Laws'})

states=counts[~counts['State'].str.contains('Fed')]

merged=pd.merge(counts,dates, on='State')
merged['Unconst. Laws per Decade']=merged['Laws']/merged['Exist Time']*10
#-------------------------------------------------------------------------------
#counts = df.groupby('col1')['col2'].value_counts()
provisions=df.groupby('State')['Constitutional Provisions Invoked'].value_counts()
provisions_grid=df.groupby('State')['Constitutional Provisions Invoked'].value_counts().unstack(fill_value=0).sort_values(by=['First Amendment','Fourteenth Amendment','Fifth Amendment','Article I, Section 8, Clause 3;Fifth Amendment','Article I, Section 10, Clause 1'])
provisions_grid_nf=df_nofed.groupby('State')['Constitutional Provisions Invoked'].value_counts().unstack(fill_value=0).sort_values(by=['First Amendment','Fourteenth Amendment','Fifth Amendment'])

provisions=provisions.rename(columns={'Constitutional Provisions Invoked':'Counts'})
provisions = provisions.reset_index()
#provisions[['State', 'Provision']] = pd.DataFrame(df['index'].tolist(), index=df.index)
provisions = provisions[['State', 'Constitutional Provisions Invoked',0]].rename(columns={'col1': 'value','Constitutional Provisions Invoked':'Provision',0:'Count'})

clauses=df.groupby('State')['Constitutional Clause(s) Invoked'].value_counts()
clauses_grid=df.groupby('State')['Constitutional Clause(s) Invoked'].value_counts().unstack(fill_value=0)
clauses=provisions.rename(columns={'Constitutional Clause(s) Invoked':'Counts'})
#clauses = clauses.reset_index()
#clauses[['State', 'Clause']] = pd.DataFrame(df['index'].tolist(), index=df.index)
#clauses = provisions[['State', 'Constitutional Clause(s) Invoked',0]].rename(columns={'col1': 'value','Constitutional Clause(s) Invoked':'Clause',0:'Count'})
subj=df_nofed.groupby('State')['Subject Matter'].value_counts().unstack(fill_value=0).sort_values(by=['Civil Rights','Criminal Law & Procedure','Taxes','Elections','Business & Corporate Law'])
sum_threshold = 4  
#unstacked = unstacked.loc[:, unstacked.sum() >= sum_threshold]
subj=subj.loc[:,subj.sum() >= sum_threshold]

summ=15
date_law=df_nofed.groupby('Date')['State'].value_counts().unstack(fill_value=0)
date_law=date_law.loc[:,date_law.sum() >= summ]

summm=6
provisions_grid=provisions_grid.loc[:,provisions_grid.sum() >= summm]
provisions_grid_nf=provisions_grid_nf.loc[:,provisions_grid_nf.sum() >= summm]






f1=plt.figure(figsize=(10,6))
a1=sns.barplot(data=counts,x='State',y='Laws',color='Gold',edgecolor='Black')
a1.set_xticklabels(a1.get_xticklabels(), rotation=90)
a1.set_xlabel('State')
a1.set_ylabel('Unconstitutional Laws Since 1803')
a1.set_title('Number of Laws Deemed Unconstitutional by State')
plt.savefig("Number of Laws Deemed Unconstitutional by State no fed.jpg", dpi=500, format="jpeg")

f2=plt.figure(figsize=(10,6))
a2=sns.barplot(data=states,x='State',y='Laws',color='Gold',edgecolor='Black')
a2.set_xlabel('State')
a2.set_ylabel('Unconstitutional Laws Since 1803')
a2.set_xticklabels(a2.get_xticklabels(), rotation=90)
a2.set_title('Number of Laws Deemed Unconstitutional by State')
plt.savefig("Number of Laws Deemed Unconstitutional by State.jpg", dpi=500, format="jpeg")


f3=plt.figure(figsize=(8,8))
a3=sns.scatterplot(data=merged,x='Date',y='Laws',color='Gold',edgecolor='Black',size='Unconst. Laws per Decade',sizes=(20,150))#,hue='State',edgecolor='Black')
a3.set_xlabel('Date Joined the Union')
a3.set_ylabel('Unconstitutional Laws Since 1803')
a3.legend(loc='upper right', bbox_to_anchor=(1.2, 1))
for i, row in merged.iterrows():
    a3.annotate(row['State'], (row['Date']+2, row['Laws']+0.5))
a3.legend(loc='center left', bbox_to_anchor=(.6, 0.8))
a3.set_title('Unconstitutional Laws by Year of Founding')
plt.savefig("Unconstitutional Laws by Year of Founding.jpg", dpi=500, format="jpeg")

merged=merged.sort_values('Unconst. Laws per Decade')
f2a=plt.figure(figsize=(12,6))
a2a=sns.barplot(data=merged,x='State Name',y='Unconst. Laws per Decade',color='Gold',edgecolor='Black')
a2a.set_xlabel('State')
a2a.set_ylabel('Unconst. Laws per Decade')
a2a.set_xticklabels(a2a.get_xticklabels(), rotation=90)
a2a.set_title('Unconstitutional Laws per Decade by State')
plt.savefig("Unconstitutional Laws per Decade by State.jpg", dpi=500, format="jpeg")

f5=plt.figure(figsize=(12,10))
a5=sns.heatmap(subj,cmap='Reds',annot=True, fmt='d')
a5.set_title('Subject Matter of Unconstitutional Laws by State')
plt.savefig("Subject Matter of Unconstitutional Laws by State.jpg", dpi=1500, format="jpeg")

f5a=plt.figure(figsize=(8,8))
a5a=sns.heatmap(date_law,cmap='Reds',annot=False)
a5a.set_ylabel('Date When Law Deemed Unconstitutional')
a5a.set_title('Unconstitutional Laws Over Time by State')
plt.savefig("Unconstitutional Laws Over Time by State.jpg", dpi=500, format="jpeg")


f5b=plt.figure(figsize=(8,10))
a5b=sns.heatmap(provisions_grid,cmap='Reds',annot=True)
a5b.set_ylabel('State')
a5b.set_title('Constitutional Provision Invoked in Overturning by State')
a5b.set_xticklabels(a5b.get_xticklabels(), rotation=90)
plt.savefig("Constitutional Provision Invoked in Overturning by State.jpg", dpi=500, format="jpeg")


f5c=plt.figure(figsize=(8,10))
a5c=sns.heatmap(provisions_grid_nf,cmap='Reds',annot=True)
a5c.set_ylabel('State')
a5c.set_title('Constitutional Provision Invoked in Overturning by State')
plt.savefig("Constitutional Provision Invoked in Overturning by State.jpg", dpi=500, format="jpeg")

#how are the counts influenced by the age of the state
#how are the counts broken down by constitutional violation
#how are the counts influenced by party of legislature at the time
# add hue for red vs blue to lmplot