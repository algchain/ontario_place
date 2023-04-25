import os,sys
import uuid
import re
import collections
import json
import random
import requests
import codecs
import time
from io import StringIO
import urllib

LOCAL_PATH = os.path.abspath(os.path.dirname(__file__))+"/"


sys.path.insert(0,LOCAL_PATH)
sys.path.insert(0,LOCAL_PATH+"../")

#0v1#  XX  Apr 25, 2023  RAW Setup  ** no time to make it clean!


'''
    TSV DATA TO WEB VIEW GITHUB PAGES
'''


def create_report():
    return

def iter_source():
    filename=LOCAL_PATH+"therme_reviews_v0413.tsv"
    c=0
    for liner in codecs.open(filename,"r","utf-8",errors="ignore").readlines():
        c+=1
        cnames=['review','rating','date','source','id']
        cols=liner.strip().split('\t')
#D        print (cols[0])
        record={}
        # Combine cnames and cols into record
        for i in range(0,len(cnames)):
            # Replace " with '
            #record[cnames[i]]=cols[i]
            record[cnames[i]]=re.sub(r'\"',"'",cols[i])
        yield record
    return

def call_dev():
    outfilename=LOCAL_PATH+"therme_reviews.html"
    fp=codecs.open(outfilename,"w","utf-8",errors="ignore")

    html=''
    html="""
    <!DOCTYPE html>
    <html>
      <head>
        <title>Ontario Place NOT Therme</title>

      <script>
      const datas = [
        """
    c=0
    for record in iter_source():
        c+=1
        html+='''["'''+str(record['review'])+'''", "'''+str(record['rating'])+'''", "'''+str(record['date'])+'''", "'''+str(record['source'])+'''", "'''+str(record['id'])+'''"],\n'''
#        if c>3:break

    html+="""

      ];
      
      function loadRandomLink() {
        // Select a random item from the datas array
        const randomItem = datas[Math.floor(Math.random() * datas.length)];
        
        // Get the link element and update its href and text attributes
        const link = document.getElementById('random-link');
        link.href = randomItem[0];
        link.textContent = randomItem[1];
      }

            function shuffleArray(array) {
        // Shuffle array in place
        for (let i = array.length - 1; i > 0; i--) {
          const j = Math.floor(Math.random() * (i + 1));
          [array[i], array[j]] = [array[j], array[i]];
        }
      }

    </script>


      </head>
    <body>
      <h1>Ontario Place NOT Therme</h1>
        <!-- Increase size of font -->
        <div style="font-size: 1.5em;">
         <p>
            Are you ready for 100 years of Therme?  Here are 8000 reasons why Therme Spas
            are hated by their customers and employees:
         </p>
        </div>

        <div style="font-size: 1em;">
         <p>
            (<a href="https://github.com/algchain/ontario_place" target="_blank">Download or share this data here</a>)
         </p>
        </div>
        <br>

    """


    html+="""

        <script>

         shuffleArray(datas);


          let linkHtml = '';
        for (const item of datas) {

          linkHtml += `

          <a href="${item[3]}" target="_blank">Review:</a>
            <!-- reduce top margin -->
             <div style="font-size: 1.5em; margin-top:-20px; padding-top:5px">
               <p>
                  ${item[0]}
                </p>
              </div>

              <div style="text-align: center;">
                  <a href="https://ontarioplaceforall.com" target="_blank" style="display: inline-block; !important; width: 30%;">Learn More</a>
                  <a href="https://forms.gle/5JGH6SX8keGm3ByF9" target="_blank" style="display: inline-block; !important; width: 30%;">Share Feedback</a>
              </div>
          
          <hr>
          `;
        }
        
        // Insert the HTML text into the body
        document.body.innerHTML += linkHtml;


    </script>

    </body>
    </html>
    """

    fp.write(html)

    fp.close()
    print ("[info] wrote: "+str(outfilename))
    return

if __name__=='__main__':
    branches=['call_dev']
    for b in branches:
        globals()[b]()
