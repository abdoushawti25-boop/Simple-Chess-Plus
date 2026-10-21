# Simple Chess Plus (Android & Web)

A complete, lightweight Android and Web chess app named **Simple Chess Plus** built with React, TypeScript, Vite, chess.js, and Capacitor.
Application ID: `com.simplechess.app`.

## Features:
1. **Playable 8x8 Chessboard:** Responsive layout optimized for mobile touch and desktop.
2. **SVG Vector Chess Pieces:** Crisp vector graphics for King, Queen, Rook, Bishop, Knight, and Pawn (White and Black) without external downloads.
3. **Legal Move Validation (chess.js):**
   * Move indicators and capture highlights.
   * Castling, En Passant, and Pawn Promotion modal.
   * Automatic Check, Checkmate, and Draw detection.
4. **Move History & Notation:** Algebraic notation strip showing moves per turn.
5. **New Game & Undo:** Restart game or undo moves at any time.
6. **Physical Sound Effects:** Move, capture, check, and game over sounds via Web Audio API.
7. **Native Android Package (Capacitor):** Configured with application ID `com.simplechess.app` and GitHub Actions automated APK workflow.

---

## Project Structure:
```
simple-chess-plus/
├── src/
│   ├── components/
│   │   └── ChessPiece.tsx     # Built-in SVG vector chess pieces
│   ├── App.tsx                # Chessboard, game state, legal moves, history, New Game
│   ├── main.tsx               # Web entry point
│   └── index.css              # Tailwind and mobile viewport styles
├── android/                   # مشروع Android الأصلي (Capacitor Native)
│   ├── app/
│   │   ├── src/main/
│   │   │   ├── java/com/simplechess/app/MainActivity.kt
│   │   │   ├── AndroidManifest.xml
│   │   │   ├── res/           # أيقونات التطبيق وثيمات الأندرويد
│   │   │   └── assets/public/ # ملفات التطبيق المجمعة للأندرويد
│   │   └── build.gradle
│   ├── build.gradle
│   └── gradlew
├── capacitor.config.ts
├── package.json
└── vite.config.ts
```

---

## كيفية تشغيل المشروع وتوليد ملف الـ APK:

### 1. تشغيل التطبيق في وضع التطوير (Web):
```bash
npm install
npm run dev
```

### 2. تجهيز وتحديث ملفات الأندرويد:
```bash
npm run build
npx cap copy android
```

### 3. بناء APK باستخدام Android Studio (الأسهل والموصى به):
1. افتح مجلد `android/` داخل برنامج **Android Studio**.
2. انتظر ثوانٍ لاكتمال مزامنة Gradle.
3. من القائمة العلوية اختر **Build > Build Bundle(s) / APK(s) > Build APK(s)**.
4. ستجد ملف الـ APK الناتج جاهزاً للتثبيت المباشر على الهاتف في المسار:
   `android/app/build/outputs/apk/debug/app-debug.apk`.

### 4. بناء APK عبر سطر الأوامر (CLI):
```bash
cd android
./gradlew assembleDebug
```
