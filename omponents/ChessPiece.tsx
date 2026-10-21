
import React from 'react';
import type { PieceSymbol } from 'chess.js';

interface ChessPieceProps {
  type: PieceSymbol;
  color: 'w' | 'b';
}

const symbols: Record<PieceSymbol, string> = {
  k: '♚',
  q: '♛',
  r: '♜',
  b: '♝',
  n: '♞',
  p: '♟'
};

export function ChessPiece({ type, color }: ChessPieceProps) {
  return (
    <span
      className={`select-none leading-none ${
        color === 'w'
          ? 'text-white'
          : 'text-slate-950'
      }`}
      style={{
        fontSize: 'clamp(20px, 8vw, 48px)',
        WebkitTextStroke: color === 'w' ? '1px #222' : '0.5px #aaa',
        textShadow: color === 'w'
          ? '0 1px 2px #333'
          : '0 1px 1px #888'
      }}
    >
      {symbols[type]}
    </span>
  );
}
