import React from 'react';

import Layout from '../components/Layout';

const IndexPage = () => (
  <Layout fullMenu>
    <article id="main">
      <header>
        <h2>CS 160</h2>
        <p>All my work from CS160</p>
      </header>
      <section className="wrapper style5">
        <div className="inner">
          <h3>Scratch</h3>
          <div>
            <ul>
              <li>
                <h5>4 Corners</h5>
               <iframe src="https://scratch.mit.edu/projects/248654347/embed" allowTransparency="true" width="485"
  height="402" frameBorder="0" scrolling="no" allowFullScreen/>
              </li>
              <li>
                <h5>Brick Breaker Game</h5>
                <iframe src="https://scratch.mit.edu/projects/108472605/embed" allowTransparency="true" width="485"
  height="402" frameBorder="0" scrolling="no" allowFullScreen/>
              </li>
              <li>
                <h5>Traverse</h5>
                <iframe src="https://scratch.mit.edu/projects/249585549/embed" allowTransparency="true" width="485"
  height="402" frameBorder="0" scrolling="no" allowFullScreen/>
              </li>
            </ul>
          </div>


          <hr />

          <h4>Python</h4>
          <ul>
            <li>
              <h5>Rock, Paper, Scissors</h5>

              <iframe src="https://trinket.io/embed/python3/4c5ad1d4b8" width="100%" height="356" frameBorder="0"
  marginWidth="0" marginHeight="0" allowFullScreen/>

            </li>
            <li>
              <h5>Average of 3 Numbers</h5>

              <iframe src="https://trinket.io/embed/python3/d027fea87d" width="100%" height="356" frameBorder="0"
  marginWidth="0" marginHeight="0" allowFullScreen/>

            </li>
            <li>
              <h5>Largest of 3 Numbers</h5>

              <iframe src="https://trinket.io/embed/python3/9c2b494ea0" width="100%" height="356" frameBorder="0"
  marginWidth="0" marginHeight="0" allowFullScreen/>

            </li>
            <li>
              <h5>Gas Milage Calculator</h5>

              <iframe src="https://trinket.io/embed/python3/e2da9bf230" width="100%" height="356" frameBorder="0"
  marginWidth="0" marginHeight="0" allowFullScreen/>

            </li>
            <li>
              <h5>Loan Calculator</h5>

              <iframe src="https://trinket.io/embed/python3/9bd1bcc986" width="100%" height="356" frameBorder="0"
  marginWidth="0" marginHeight="0" allowFullScreen/>

            </li>
            <li>
              <h5>Hangman</h5>

              <iframe src="https://trinket.io/embed/python3/44e1301053" width="100%" height="356" frameBorder="0"
  marginWidth="0" marginHeight="0" allowFullScreen/>

            </li>
            <li>
              <h5>Base 10 to base 2 through 16</h5>

              <iframe src="https://trinket.io/embed/python3/6f4d106da5" width="100%" height="356" frameBorder="0"
  marginWidth="0" marginHeight="0" allowFullScreen/>

            </li>
            <li>
              <h5>Master Mind</h5>


              <iframe src="https://trinket.io/embed/python3/7f72f62cc6" width="100%" height="356" frameBorder="0"
  marginWidth="0" marginHeight="0" allowFullScreen/>


            </li>
          </ul>
          <h3>Code HS</h3>
          <h3>P5 js</h3>
        </div>
      </section>
    </article>
  </Layout>
);

export default IndexPage;
