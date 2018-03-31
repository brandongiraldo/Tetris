import * as React from "react";
import {render} from 'react-dom';
import Board from './src/components/board/board'
import Cell from './src/components/cell/cell'

render(
  <div>
    <div>Welcome home!</div>
    <Board />
    <Cell />
  </div>,
  document.getElementById('root'),
);