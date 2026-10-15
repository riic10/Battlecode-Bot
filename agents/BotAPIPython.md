# CAMBC Bot API — Python

Event: cambc2026a. Read alongside GameRules.md. Signatures and descriptions come from the same SDK documentation shown on the Bot API page.

Examples are fragments for an initialised bot. Check visibility and action preconditions. 

```python
import cambc as bc
```

## cambc

### champions

```python
def champions(team: Optional[Team] = None) -> list[Champion]
```

Visible champions of a team, or of both teams (allies first). Args: team: Team to include, or None for both teams.

Use this value in your bot's draft or turn logic.

Inputs:
- team: Optional[Team]

```python
result = bc.champions(team)
```

### end_turn

```python
def end_turn() -> None
```

End the current turn.

Stop optional planning when little fuel remains and yield the current turn.

```python
if bc.fuel_remaining() < 1000:
    bc.end_turn()
```

### fuel_remaining

```python
def fuel_remaining() -> int
```

Return the fuel left in the current turn.

Stop optional planning when little fuel remains and yield the current turn.

```python
if bc.fuel_remaining() < 1000:
    bc.end_turn()
```

### global_submitted_gems

```python
def global_submitted_gems(team: Team) -> int
```

Return the total gems a team has tributed. Args: team: Team to count.

Use this value in your bot's draft or turn logic.

Inputs:
- team: Team

```python
result = bc.global_submitted_gems(team)
```

### is_draft

```python
def is_draft() -> bool
```

Return whether this bot instance is running the draft rather than controlling a champion.

Use this value in your bot's draft or turn logic.

```python
is_draft = bc.is_draft()
```

### me

```python
def me() -> Champion
```

This bot's champion; raises ValueError during the draft.

Use this value in your bot's draft or turn logic.

```python
result = bc.me()
```

### resign

```python
def resign() -> None
```



Use this value in your bot's draft or turn logic.

```python
bc.resign()
```

### round_number

```python
def round_number() -> int
```

Return the current round number.

Use this value in your bot's draft or turn logic.

```python
result = bc.round_number()
```

## cambc.Ability

### __eq__

```python
def __eq__(self, other: object) -> bool
```



### __hash__

```python
def __hash__(self) -> int
```



### __init__

```python
def __init__(self) -> None
```



This view cannot be constructed directly. Obtain it from the SDK when inspecting the current turn or map.

```python
ability = bc.me().abilities()[0]
```

### __repr__

```python
def __repr__(self) -> str
```



### can_target_allies

```python
def can_target_allies(self) -> bool
```

Return whether the ability can target allied champions.

Evaluate an ability before choosing a spell.

```python
subject = bc.me().abilities()[0]

can_target_allies = subject.can_target_allies()
```

### can_target_camps

```python
def can_target_camps(self) -> bool
```

Return whether the ability can target camps.

Evaluate an ability before choosing a spell.

```python
subject = bc.me().abilities()[0]

can_target_camps = subject.can_target_camps()
```

### can_target_enemies

```python
def can_target_enemies(self) -> bool
```

Return whether the ability can target enemy champions.

Evaluate an ability before choosing a spell.

```python
subject = bc.me().abilities()[0]

can_target_enemies = subject.can_target_enemies()
```

### can_target_ground

```python
def can_target_ground(self) -> bool
```

Return whether the ability can target a tile.

Evaluate an ability before choosing a spell.

```python
subject = bc.me().abilities()[0]

can_target_ground = subject.can_target_ground()
```

### can_target_self

```python
def can_target_self(self) -> bool
```

Return whether the ability can target its caster.

Evaluate an ability before choosing a spell.

```python
subject = bc.me().abilities()[0]

can_target_self = subject.can_target_self()
```

### cooldown

```python
def cooldown(self) -> int
```

Return the remaining cooldown; 0 means ready.

Evaluate an ability before choosing a spell.

```python
subject = bc.me().abilities()[0]

result = subject.cooldown()
```

### damage_amount

```python
def damage_amount(self, target: Optional[Champion] = None) -> float
```

Return the damage the ability would deal, after mitigation and shields if a target is given. Args: target: Optional visible champion that would be hit.

Evaluate an ability before choosing a spell.

Inputs:
- target: Optional[Champion]

```python
subject = bc.me().abilities()[0]

result = subject.damage_amount(target)
```

### get

```python
def get(self, kind: type[_A]) -> _A
```

Return the ability's payload of the requested kind; raises if the slot holds a different kind. Args: kind: Ability kind to extract.

Evaluate an ability before choosing a spell.

Inputs:
- kind: type[_A]

```python
subject = bc.me().abilities()[0]

result = subject.get(kind)
```

### has

```python
def has(self, kind: Union[AbilityKind, type[AbilityInfo]]) -> bool
```

Return whether the slot holds an ability of a kind. Args: kind: Ability kind to test for.

Evaluate an ability before choosing a spell.

Inputs:
- kind: Union[AbilityKind, type[AbilityInfo]]

```python
subject = bc.me().abilities()[0]

result = subject.has(kind)
```

### heal_amount

```python
def heal_amount(self, target: Optional[Champion] = None) -> float
```

Return the healing the ability would do, capped at the target's missing health if a target is given. Args: target: Optional visible champion that would be healed.

Evaluate an ability before choosing a spell.

Inputs:
- target: Optional[Champion]

```python
subject = bc.me().abilities()[0]

result = subject.heal_amount(target)
```

### info

```python
def info(self, kind: Optional[AbilityKind] = None) -> Optional[AbilityInfo]
```

Ability properties, or None for an empty slot; with kind, require that kind. Args: kind: Optional ability kind the slot must have; raises if it differs.

Evaluate an ability before choosing a spell.

Inputs:
- kind: Optional[AbilityKind]

```python
subject = bc.me().abilities()[0]

result = subject.info(kind)
```

### is_aoe_damage

```python
def is_aoe_damage(self) -> bool
```

Check whether this is an area-damage ability.

Evaluate an ability before choosing a spell.

```python
subject = bc.me().abilities()[0]

is_aoe_damage = subject.is_aoe_damage()
```

### is_attack_reset

```python
def is_attack_reset(self) -> bool
```

Check whether this is an attack-reset ability.

Evaluate an ability before choosing a spell.

```python
subject = bc.me().abilities()[0]

is_attack_reset = subject.is_attack_reset()
```

### is_cc

```python
def is_cc(self) -> bool
```

Check whether this is a crowd-control ability.

Evaluate an ability before choosing a spell.

```python
subject = bc.me().abilities()[0]

is_cc = subject.is_cc()
```

### is_damage

```python
def is_damage(self) -> bool
```

Check whether this is a damage ability.

Evaluate an ability before choosing a spell.

```python
subject = bc.me().abilities()[0]

is_damage = subject.is_damage()
```

### is_dash

```python
def is_dash(self) -> bool
```

Check whether this is a dash ability.

Evaluate an ability before choosing a spell.

```python
subject = bc.me().abilities()[0]

is_dash = subject.is_dash()
```

### is_heal

```python
def is_heal(self) -> bool
```

Check whether this is a healing ability.

Evaluate an ability before choosing a spell.

```python
subject = bc.me().abilities()[0]

is_heal = subject.is_heal()
```

### is_on_cooldown

```python
def is_on_cooldown(self) -> bool
```

Return whether the cooldown is still running.

Evaluate an ability before choosing a spell.

```python
subject = bc.me().abilities()[0]

is_on_cooldown = subject.is_on_cooldown()
```

### is_ready

```python
def is_ready(self) -> bool
```

Check whether this ability is ready to cast.

Evaluate an ability before choosing a spell.

```python
subject = bc.me().abilities()[0]

is_ready = subject.is_ready()
```

### is_shield

```python
def is_shield(self) -> bool
```

Check whether this is a shield ability.

Evaluate an ability before choosing a spell.

```python
subject = bc.me().abilities()[0]

is_shield = subject.is_shield()
```

### mask_into

```python
def mask_into(self, out: Bitboard) -> None
```

Like valid_tiles, but writes into out. Args: out: Destination Bitboard; its previous contents are overwritten.

Evaluate an ability before choosing a spell.

Inputs:
- out: Bitboard

```python
subject = bc.me().abilities()[0]

subject.mask_into(out)
```

### shield_amount

```python
def shield_amount(self, target: Optional[Champion] = None) -> float
```

Return the shield the ability would grant. Args: target: Optional visible champion that would be shielded.

Evaluate an ability before choosing a spell.

Inputs:
- target: Optional[Champion]

```python
subject = bc.me().abilities()[0]

result = subject.shield_amount(target)
```

### slot

```python
def slot(self) -> int
```

Return the ability's slot index on its champion.

Evaluate an ability before choosing a spell.

```python
subject = bc.me().abilities()[0]

result = subject.slot()
```

### use

```python
def use(self, target: Optional[Union[Unit, Vec2]] = None) -> bool
```

Cast on a unit, at a ground tile, or without a target. Unit casts land on the target's tile. Returns False for a newly revealed obstruction; known invalid targets raise Error. Args: target: Champion or camp to cast on, a tile to cast at, or None for an untargeted ability.

Evaluate an ability before choosing a spell.

Inputs:
- target: Optional[Union[Unit, Vec2]]

```python
subject = bc.me().abilities()[0]

result = subject.use(target)
```

### valid_targets

```python
def valid_targets(self) -> AbilityTargetMask
```

Return the categories of target the ability accepts.

Evaluate an ability before choosing a spell.

```python
subject = bc.me().abilities()[0]

result = subject.valid_targets()
```

### valid_tiles

```python
def valid_tiles(self) -> Bitboard
```

Return the tiles within casting range; does not check visibility or occupancy.

Evaluate an ability before choosing a spell.

```python
subject = bc.me().abilities()[0]

result = subject.valid_tiles()
```

## cambc.AbilityKind

### to_string

```python
def to_string(value: int) -> str
```



## cambc.AbilityTargetMask

### __and__

```python
def __and__(self, other: int) -> Self
```



Evaluate an ability before choosing a spell.

Inputs:
- other: int

```python
subject = bc.me().abilities()[0].valid_targets()

result = subject & other
```

### __contains__

```python
def __contains__(self, flags: Self) -> bool
```



Evaluate an ability before choosing a spell.

Inputs:
- flags: Self

```python
subject = bc.me().abilities()[0].valid_targets()

result = flags in subject
```

### __invert__

```python
def __invert__(self) -> Self
```



Evaluate an ability before choosing a spell.

```python
subject = bc.me().abilities()[0].valid_targets()

result = ~subject
```

### __iter__

```python
def __iter__(self) -> Iterator[Self]
```



Evaluate an ability before choosing a spell.

```python
subject = bc.me().abilities()[0].valid_targets()

result = iter(subject)
```

### __or__

```python
def __or__(self, other: int) -> Self
```



Evaluate an ability before choosing a spell.

Inputs:
- other: int

```python
subject = bc.me().abilities()[0].valid_targets()

result = subject | other
```

### __rand__

```python
def __rand__(self, other: int) -> Self
```



Evaluate an ability before choosing a spell.

Inputs:
- other: int

```python
subject = bc.me().abilities()[0].valid_targets()

result = subject.__rand__(other)
```

### __ror__

```python
def __ror__(self, other: int) -> Self
```



Evaluate an ability before choosing a spell.

Inputs:
- other: int

```python
subject = bc.me().abilities()[0].valid_targets()

result = subject.__ror__(other)
```

### __rsub__

```python
def __rsub__(self, other: int) -> Self
```



Evaluate an ability before choosing a spell.

Inputs:
- other: int

```python
subject = bc.me().abilities()[0].valid_targets()

result = subject.__rsub__(other)
```

### __rxor__

```python
def __rxor__(self, other: int) -> Self
```



Evaluate an ability before choosing a spell.

Inputs:
- other: int

```python
subject = bc.me().abilities()[0].valid_targets()

result = subject.__rxor__(other)
```

### __sub__

```python
def __sub__(self, other: int) -> Self
```



Evaluate an ability before choosing a spell.

Inputs:
- other: int

```python
subject = bc.me().abilities()[0].valid_targets()

result = subject - other
```

### __xor__

```python
def __xor__(self, other: int) -> Self
```



Evaluate an ability before choosing a spell.

Inputs:
- other: int

```python
subject = bc.me().abilities()[0].valid_targets()

result = subject ^ other
```

### all

```python
def all(cls) -> Self
```

Return a set with every named flag.

Evaluate an ability before choosing a spell.

```python
subject = bc.me().abilities()[0].valid_targets()

result = subject.all()
```

### empty

```python
def empty(cls) -> Self
```

Return a set with no flags.

Evaluate an ability before choosing a spell.

```python
subject = bc.me().abilities()[0].valid_targets()

result = subject.empty()
```

### from_bits

```python
def from_bits(cls, bits: int) -> Optional[Self]
```

Return the set for raw bits, or None if any bit is not a named flag. Args: bits: Raw flag bits.

Evaluate an ability before choosing a spell.

Inputs:
- bits: int

```python
subject = bc.me().abilities()[0].valid_targets()

result = subject.from_bits(bits)
```

### from_bits_truncate

```python
def from_bits_truncate(cls, bits: int) -> Self
```

Return the set for raw bits, dropping bits that are not named flags. Args: bits: Raw flag bits.

Evaluate an ability before choosing a spell.

Inputs:
- bits: int

```python
subject = bc.me().abilities()[0].valid_targets()

result = subject.from_bits_truncate(bits)
```

### intersects

```python
def intersects(self, flags: Self) -> bool
```

Return whether this set shares any flag with flags. Args: flags: Flags to test.

Evaluate an ability before choosing a spell.

Inputs:
- flags: Self

```python
subject = bc.me().abilities()[0].valid_targets()

result = subject.intersects(flags)
```

### is_all

```python
def is_all(self) -> bool
```

Return whether every named flag is set.

Evaluate an ability before choosing a spell.

```python
subject = bc.me().abilities()[0].valid_targets()

is_all = subject.is_all()
```

## cambc.AltarLock

### hits_remaining

```python
def hits_remaining(self) -> int
```

Return how many hits the altar lock can still take.

Use this value in your bot's draft or turn logic.

Inputs:
- subject: bc.AltarLock (a valid instance)

```python
result = subject.hits_remaining()
```

### is_ally

```python
def is_ally(self) -> bool
```

Check whether this altar lock belongs to the observing team.

Use this value in your bot's draft or turn logic.

Inputs:
- subject: bc.AltarLock (a valid instance)

```python
is_ally = subject.is_ally()
```

### is_enemy

```python
def is_enemy(self) -> bool
```

Check whether this altar lock belongs to the opposing team.

Use this value in your bot's draft or turn logic.

Inputs:
- subject: bc.AltarLock (a valid instance)

```python
is_enemy = subject.is_enemy()
```

### position

```python
def position(self) -> Vec2
```

Return the altar lock's tile.

Use this value in your bot's draft or turn logic.

Inputs:
- subject: bc.AltarLock (a valid instance)

```python
result = subject.position()
```

### team

```python
def team(self) -> Team
```

Return the team that owns the altar lock.

Use this value in your bot's draft or turn logic.

Inputs:
- subject: bc.AltarLock (a valid instance)

```python
result = subject.team()
```

## cambc.Bitboard

### __and__

```python
def __and__(self, other: Bitboard) -> Bitboard
```



Build a pathfinding or targeting mask.

Inputs:
- other: Bitboard

```python
subject = bc.game_map.walls()

result = subject & other
```

### __eq__

```python
def __eq__(self, other: object) -> bool
```



### __iand__

```python
def __iand__(self, other: Bitboard) -> Self
```



Build a pathfinding or targeting mask.

Inputs:
- other: Bitboard

```python
subject = bc.game_map.walls()

result = subject.__iand__(other)
```

### __init__

```python
def __init__(self) -> None
```



Build a pathfinding or targeting mask.

```python
result = bc.Bitboard()
```

### __invert__

```python
def __invert__(self) -> Bitboard
```



Build a pathfinding or targeting mask.

```python
subject = bc.game_map.walls()

result = ~subject
```

### __ior__

```python
def __ior__(self, other: Bitboard) -> Self
```



Build a pathfinding or targeting mask.

Inputs:
- other: Bitboard

```python
subject = bc.game_map.walls()

result = subject.__ior__(other)
```

### __ixor__

```python
def __ixor__(self, other: Bitboard) -> Self
```



Build a pathfinding or targeting mask.

Inputs:
- other: Bitboard

```python
subject = bc.game_map.walls()

result = subject.__ixor__(other)
```

### __or__

```python
def __or__(self, other: Bitboard) -> Bitboard
```



Build a pathfinding or targeting mask.

Inputs:
- other: Bitboard

```python
subject = bc.game_map.walls()

result = subject | other
```

### __xor__

```python
def __xor__(self, other: Bitboard) -> Bitboard
```



Build a pathfinding or targeting mask.

Inputs:
- other: Bitboard

```python
subject = bc.game_map.walls()

result = subject ^ other
```

### clear

```python
def clear(self) -> None
```

Clear every tile.

Build a pathfinding or targeting mask.

```python
subject = bc.game_map.walls()

subject.clear()
```

### copy

```python
def copy(self) -> Bitboard
```

Return an independent copy.

Build a pathfinding or targeting mask.

```python
subject = bc.game_map.walls()

result = subject.copy()
```

### count

```python
def count(self) -> int
```

Return the number of set tiles.

Build a pathfinding or targeting mask.

```python
subject = bc.game_map.walls()

result = subject.count()
```

### draw_chebyshev

```python
def draw_chebyshev(self, center: Vec2, radius: float) -> None
```

Set every tile within a Chebyshev radius of a centre tile. Args: center: Centre tile. radius: Chebyshev radius in tiles.

Build a pathfinding or targeting mask.

Inputs:
- center: Vec2
- radius: float

```python
subject = bc.game_map.walls()

subject.draw_chebyshev(center, radius)
```

### draw_circle

```python
def draw_circle(self, center: Vec2, radius: float) -> None
```

Set every tile within a Euclidean radius of a centre tile. Args: center: Centre tile. radius: Euclidean radius in tiles.

Build a pathfinding or targeting mask.

Inputs:
- center: Vec2
- radius: float

```python
subject = bc.game_map.walls()

subject.draw_circle(center, radius)
```

### export_linear_buffer

```python
def export_linear_buffer(self) -> bytes
```

Return the contents as a row-major buffer with one value per tile.

Build a pathfinding or targeting mask.

```python
subject = bc.game_map.walls()

result = subject.export_linear_buffer()
```

### export_linear_buffer_into

```python
def export_linear_buffer_into(self, out: Buffer) -> None
```

Write the contents as a row-major buffer with one value per tile. Args: out: Writable bytes-like object exactly linear_buffer_size() long.

Build a pathfinding or targeting mask.

Inputs:
- out: Buffer

```python
subject = bc.game_map.walls()

subject.export_linear_buffer_into(out)
```

### export_raw_buffer

```python
def export_raw_buffer(self) -> bytes
```

Return the contents as an engine-chunked buffer.

Build a pathfinding or targeting mask.

```python
subject = bc.game_map.walls()

result = subject.export_raw_buffer()
```

### export_raw_buffer_into

```python
def export_raw_buffer_into(self, out: Buffer) -> None
```

Write the contents as an engine-chunked buffer. Args: out: Writable bytes-like object exactly raw_buffer_size() long.

Build a pathfinding or targeting mask.

Inputs:
- out: Buffer

```python
subject = bc.game_map.walls()

subject.export_raw_buffer_into(out)
```

### fill

```python
def fill(self) -> None
```

Set every tile on the map.

Build a pathfinding or targeting mask.

```python
subject = bc.game_map.walls()

subject.fill()
```

### height

```python
def height(self) -> int
```

Return the map height in tiles.

### import_linear_buffer

```python
def import_linear_buffer(self, data: Buffer) -> None
```

Replace the contents from a row-major buffer with one value per tile. Args: data: Bytes-like object exactly linear_buffer_size() long.

Build a pathfinding or targeting mask.

Inputs:
- data: Buffer

```python
subject = bc.game_map.walls()

subject.import_linear_buffer(data)
```

### import_raw_buffer

```python
def import_raw_buffer(self, data: Buffer) -> None
```

Replace the contents from an engine-chunked buffer. Args: data: Bytes-like object exactly raw_buffer_size() long.

Build a pathfinding or targeting mask.

Inputs:
- data: Buffer

```python
subject = bc.game_map.walls()

subject.import_raw_buffer(data)
```

### is_empty

```python
def is_empty(self) -> bool
```

Return whether no tile is set.

Build a pathfinding or targeting mask.

```python
subject = bc.game_map.walls()

is_empty = subject.is_empty()
```

### is_set

```python
def is_set(self, position: Vec2) -> bool
```

Return whether the tile is set; raises Error outside the map. Args: position: Tile to query.

Build a pathfinding or targeting mask.

Inputs:
- position: Vec2

```python
subject = bc.game_map.walls()

is_set = subject.is_set(position)
```

### linear_buffer_size

```python
def linear_buffer_size() -> int
```

Return the size in bytes of the row-major buffer.

Build a pathfinding or targeting mask.

```python
result = bc.Bitboard.linear_buffer_size()
```

### positions

```python
def positions(self) -> list[Vec2]
```

Return the set tiles in row-major order.

Build a pathfinding or targeting mask.

```python
subject = bc.game_map.walls()

result = subject.positions()
```

### print

```python
def print(self) -> None
```

Print this board to stdout for debugging.

Build a pathfinding or targeting mask.

```python
subject = bc.game_map.walls()

subject.print()
```

### raw_buffer_size

```python
def raw_buffer_size() -> int
```

Return the size in bytes of the engine-chunked buffer.

Build a pathfinding or targeting mask.

```python
result = bc.Bitboard.raw_buffer_size()
```

### reachable_tiles

```python
def reachable_tiles( self, origin: Vec2, distance: int, frontier: Optional[Bitboard] = None, scratch: Optional[Bitboard] = None ) -> Bitboard
```

Return the tiles reachable from origin, treating this board as walls. Args: origin: Start tile. distance: Maximum number of 8-directional steps from origin. frontier: Optional working Bitboard; its contents are overwritten. scratch: Optional working Bitboard; its contents are overwritten.

Build a pathfinding or targeting mask.

Inputs:
- origin: Vec2
- distance: int
- frontier: Optional[Bitboard]
- scratch: Optional[Bitboard]

```python
result = bc.Bitboard.reachable_tiles(origin, distance, frontier, scratch)
```

### reachable_tiles_into

```python
def reachable_tiles_into( self, origin: Vec2, distance: int, out: Bitboard, frontier: Optional[Bitboard] = None, scratch: Optional[Bitboard] = None ) -> None
```

Like reachable_tiles, but writes into out. Args: origin: Start tile. distance: Maximum number of 8-directional steps from origin. out: Destination; its previous contents are overwritten. frontier: Optional working Bitboard; its contents are overwritten. scratch: Optional working Bitboard; its contents are overwritten.

Build a pathfinding or targeting mask.

Inputs:
- origin: Vec2
- distance: int
- out: Bitboard
- frontier: Optional[Bitboard]
- scratch: Optional[Bitboard]

```python
bc.Bitboard.reachable_tiles_into(origin, distance, out, frontier, scratch)
```

### reflect

```python
def reflect(self, symmetry: int) -> Bitboard
```

Return a copy transformed by a map symmetry. Args: symmetry: Map symmetry to apply.

Build a pathfinding or targeting mask.

Inputs:
- symmetry: int

```python
subject = bc.game_map.walls()

result = subject.reflect(symmetry)
```

### reflect_horizontal

```python
def reflect_horizontal(self) -> Bitboard
```

Return a copy reflected across the map horizontally, reversing x.

Build a pathfinding or targeting mask.

```python
subject = bc.game_map.walls()

result = subject.reflect_horizontal()
```

### reflect_horizontal_into

```python
def reflect_horizontal_into(self, out: Bitboard) -> None
```

Like reflect_horizontal, but writes into out. Args: out: Destination; its previous contents are overwritten.

Build a pathfinding or targeting mask.

Inputs:
- out: Bitboard

```python
subject = bc.game_map.walls()

subject.reflect_horizontal_into(out)
```

### reflect_into

```python
def reflect_into(self, symmetry: int, out: Bitboard) -> None
```

Like reflect, but writes into out. Args: symmetry: Map symmetry to apply. out: Destination; its previous contents are overwritten.

Build a pathfinding or targeting mask.

Inputs:
- symmetry: int
- out: Bitboard

```python
subject = bc.game_map.walls()

subject.reflect_into(symmetry, out)
```

### reflect_vertical

```python
def reflect_vertical(self) -> Bitboard
```

Return a copy reflected across the map vertically, reversing y.

Build a pathfinding or targeting mask.

```python
subject = bc.game_map.walls()

result = subject.reflect_vertical()
```

### reflect_vertical_into

```python
def reflect_vertical_into(self, out: Bitboard) -> None
```

Like reflect_vertical, but writes into out. Args: out: Destination; its previous contents are overwritten.

Build a pathfinding or targeting mask.

Inputs:
- out: Bitboard

```python
subject = bc.game_map.walls()

subject.reflect_vertical_into(out)
```

### rotate_180

```python
def rotate_180(self) -> Bitboard
```

Return a copy rotated 180 degrees within the map.

Build a pathfinding or targeting mask.

```python
subject = bc.game_map.walls()

result = subject.rotate_180()
```

### rotate_180_into

```python
def rotate_180_into(self, out: Bitboard) -> None
```

Like rotate_180, but writes into out. Args: out: Destination; its previous contents are overwritten.

Build a pathfinding or targeting mask.

Inputs:
- out: Bitboard

```python
subject = bc.game_map.walls()

subject.rotate_180_into(out)
```

### set

```python
def set(self, position: Vec2, value: bool = True) -> None
```

Set or clear a tile; raises Error outside the map. Args: position: Tile to update. value: True to set the tile, False to clear it.

Build a pathfinding or targeting mask.

Inputs:
- position: Vec2
- value: bool

```python
subject = bc.game_map.walls()

subject.set(position, value)
```

### shadow_cast

```python
def shadow_cast(self, origin: Vec2, distance: int) -> Bitboard
```

Return the tiles visible from origin, treating this board as opaque walls. Args: origin: Viewer tile. distance: Maximum sight radius in tiles.

Build a pathfinding or targeting mask.

Inputs:
- origin: Vec2
- distance: int

```python
subject = bc.game_map.walls()

result = subject.shadow_cast(origin, distance)
```

### shadow_cast_into

```python
def shadow_cast_into(self, origin: Vec2, distance: int, out: Bitboard) -> None
```

Like shadow_cast, but writes into out. Args: origin: Viewer tile. distance: Maximum sight radius in tiles. out: Destination; its previous contents are overwritten.

Build a pathfinding or targeting mask.

Inputs:
- origin: Vec2
- distance: int
- out: Bitboard

```python
subject = bc.game_map.walls()

subject.shadow_cast_into(origin, distance, out)
```

### shift_right

```python
def shift_right(self, count: int) -> Bitboard
```

Return a copy shifted horizontally; tiles shifted off the map are dropped. Args: count: Columns to shift; negative values shift left.

Build a pathfinding or targeting mask.

Inputs:
- count: int

```python
subject = bc.game_map.walls()

result = subject.shift_right(count)
```

### shift_right_into

```python
def shift_right_into(self, count: int, out: Bitboard) -> None
```

Like shift_right, but writes into out. Args: count: Columns to shift; negative values shift left. out: Destination; its previous contents are overwritten.

Build a pathfinding or targeting mask.

Inputs:
- count: int
- out: Bitboard

```python
subject = bc.game_map.walls()

subject.shift_right_into(count, out)
```

### shift_up

```python
def shift_up(self, count: int) -> Bitboard
```

Return a copy shifted vertically; tiles shifted off the map are dropped. Args: count: Rows to shift; negative values shift down.

Build a pathfinding or targeting mask.

Inputs:
- count: int

```python
subject = bc.game_map.walls()

result = subject.shift_up(count)
```

### shift_up_into

```python
def shift_up_into(self, count: int, out: Bitboard) -> None
```

Like shift_up, but writes into out. Args: count: Rows to shift; negative values shift down. out: Destination; its previous contents are overwritten.

Build a pathfinding or targeting mask.

Inputs:
- count: int
- out: Bitboard

```python
subject = bc.game_map.walls()

subject.shift_up_into(count, out)
```

### toggle

```python
def toggle(self, position: Vec2) -> None
```

Flip a tile; raises Error outside the map. Args: position: Tile to flip.

Build a pathfinding or targeting mask.

Inputs:
- position: Vec2

```python
subject = bc.game_map.walls()

subject.toggle(position)
```

### width

```python
def width(self) -> int
```

Return the map width in tiles.

## cambc.BuffCollection

### __init__

```python
def __init__(self, buffs: list[Optional[Buff]], present: tuple[Buff, ...]) -> None
```



Inspect a visible unit's active effects when evaluating a fight.

Inputs:
- buffs: list[Optional[Buff]]
- present: tuple[Buff, ...]

```python
result = bc.BuffCollection(buffs, present)
```

### __iter__

```python
def __iter__(self) -> Iterator[Buff]
```



Inspect a visible unit's active effects when evaluating a fight.

```python
subject = bc.me().buffs()

result = iter(subject)
```

### __len__

```python
def __len__(self) -> int
```



### get

```python
def get(self, kind: Union[int, type[Buff]]) -> Buff
```

Return the captured buff of a kind; raises KeyError if it was absent. Args: kind: Buff kind to look up.

Inspect a visible unit's active effects when evaluating a fight.

Inputs:
- kind: Union[int, type[Buff]]

```python
subject = bc.me().buffs()

result = subject.get(kind)
```

### has

```python
def has(self, kind: Union[int, type[Buff]]) -> bool
```

Return whether a buff of a kind was active when the collection was captured. Args: kind: Buff kind to test for.

Inspect a visible unit's active effects when evaluating a fight.

Inputs:
- kind: Union[int, type[Buff]]

```python
subject = bc.me().buffs()

result = subject.has(kind)
```

### has_enhanced_attack

```python
def has_enhanced_attack(self) -> bool
```

Check whether the captured collection has an enhanced-attack buff.

Inspect a visible unit's active effects when evaluating a fight.

```python
subject = bc.me().buffs()

has_enhanced_attack = subject.has_enhanced_attack()
```

### has_shield

```python
def has_shield(self) -> bool
```

Check whether the captured collection has a shield buff.

Inspect a visible unit's active effects when evaluating a fight.

```python
subject = bc.me().buffs()

has_shield = subject.has_shield()
```

### has_stun

```python
def has_stun(self) -> bool
```

Check whether the captured collection has a stun buff.

Inspect a visible unit's active effects when evaluating a fight.

```python
subject = bc.me().buffs()

has_stun = subject.has_stun()
```

### is_empty

```python
def is_empty(self) -> bool
```

Return whether no buffs were active when the collection was captured.

Inspect a visible unit's active effects when evaluating a fight.

```python
subject = bc.me().buffs()

is_empty = subject.is_empty()
```

## cambc.BuffRestrictions

### __and__

```python
def __and__(self, other: int) -> Self
```



Combine or inspect flags before deciding which actions or targets are allowed.

Inputs:
- other: int

```python
subject = bc.me().restrictions()

result = subject & other
```

### __contains__

```python
def __contains__(self, flags: Self) -> bool
```



Combine or inspect flags before deciding which actions or targets are allowed.

Inputs:
- flags: Self

```python
subject = bc.me().restrictions()

result = flags in subject
```

### __invert__

```python
def __invert__(self) -> Self
```



Combine or inspect flags before deciding which actions or targets are allowed.

```python
subject = bc.me().restrictions()

result = ~subject
```

### __iter__

```python
def __iter__(self) -> Iterator[Self]
```



Combine or inspect flags before deciding which actions or targets are allowed.

```python
subject = bc.me().restrictions()

result = iter(subject)
```

### __or__

```python
def __or__(self, other: int) -> Self
```



Combine or inspect flags before deciding which actions or targets are allowed.

Inputs:
- other: int

```python
subject = bc.me().restrictions()

result = subject | other
```

### __rand__

```python
def __rand__(self, other: int) -> Self
```



Combine or inspect flags before deciding which actions or targets are allowed.

Inputs:
- other: int

```python
subject = bc.me().restrictions()

result = subject.__rand__(other)
```

### __ror__

```python
def __ror__(self, other: int) -> Self
```



Combine or inspect flags before deciding which actions or targets are allowed.

Inputs:
- other: int

```python
subject = bc.me().restrictions()

result = subject.__ror__(other)
```

### __rsub__

```python
def __rsub__(self, other: int) -> Self
```



Combine or inspect flags before deciding which actions or targets are allowed.

Inputs:
- other: int

```python
subject = bc.me().restrictions()

result = subject.__rsub__(other)
```

### __rxor__

```python
def __rxor__(self, other: int) -> Self
```



Combine or inspect flags before deciding which actions or targets are allowed.

Inputs:
- other: int

```python
subject = bc.me().restrictions()

result = subject.__rxor__(other)
```

### __sub__

```python
def __sub__(self, other: int) -> Self
```



Combine or inspect flags before deciding which actions or targets are allowed.

Inputs:
- other: int

```python
subject = bc.me().restrictions()

result = subject - other
```

### __xor__

```python
def __xor__(self, other: int) -> Self
```



Combine or inspect flags before deciding which actions or targets are allowed.

Inputs:
- other: int

```python
subject = bc.me().restrictions()

result = subject ^ other
```

### all

```python
def all(cls) -> Self
```

Return a set with every named flag.

Combine or inspect flags before deciding which actions or targets are allowed.

```python
subject = bc.me().restrictions()

result = subject.all()
```

### empty

```python
def empty(cls) -> Self
```

Return a set with no flags.

Combine or inspect flags before deciding which actions or targets are allowed.

```python
subject = bc.me().restrictions()

result = subject.empty()
```

### from_bits

```python
def from_bits(cls, bits: int) -> Optional[Self]
```

Return the set for raw bits, or None if any bit is not a named flag. Args: bits: Raw flag bits.

Combine or inspect flags before deciding which actions or targets are allowed.

Inputs:
- bits: int

```python
subject = bc.me().restrictions()

result = subject.from_bits(bits)
```

### from_bits_truncate

```python
def from_bits_truncate(cls, bits: int) -> Self
```

Return the set for raw bits, dropping bits that are not named flags. Args: bits: Raw flag bits.

Combine or inspect flags before deciding which actions or targets are allowed.

Inputs:
- bits: int

```python
subject = bc.me().restrictions()

result = subject.from_bits_truncate(bits)
```

### intersects

```python
def intersects(self, flags: Self) -> bool
```

Return whether this set shares any flag with flags. Args: flags: Flags to test.

Combine or inspect flags before deciding which actions or targets are allowed.

Inputs:
- flags: Self

```python
subject = bc.me().restrictions()

result = subject.intersects(flags)
```

### is_all

```python
def is_all(self) -> bool
```

Return whether every named flag is set.

Combine or inspect flags before deciding which actions or targets are allowed.

```python
subject = bc.me().restrictions()

is_all = subject.is_all()
```

## cambc.BuffTypes

### to_string

```python
def to_string(value: int) -> str
```



## cambc.Camp

### __eq__

```python
def __eq__(self, other: object) -> bool
```



### __hash__

```python
def __hash__(self) -> int
```



### __index__

```python
def __index__(self) -> int
```



### __repr__

```python
def __repr__(self) -> str
```



### attack_range

```python
def attack_range(self) -> int
```

Return the attack range in Chebyshev tiles; melee camps have range 1.

Evaluate a visible camp before choosing where to farm.

Inputs:
- subject: bc.Camp (a valid instance)

```python
result = subject.attack_range()
```

### base_stats

```python
def base_stats(self) -> CampStats
```

Return the camp type's design stats.

Evaluate a visible camp before choosing where to farm.

Inputs:
- subject: bc.Camp (a valid instance)

```python
result = subject.base_stats()
```

### camp_group

```python
def camp_group(self) -> game_map.CampGroup
```

Return the group this camp belongs to.

Evaluate a visible camp before choosing where to farm.

Inputs:
- subject: bc.Camp (a valid instance)

```python
result = subject.camp_group()
```

### focus

```python
def focus(self) -> float
```

Return current focus; raises Error if the unit is not visible.

Evaluate a visible camp before choosing where to farm.

Inputs:
- subject: bc.Camp (a valid instance)

```python
result = subject.focus()
```

### health

```python
def health(self) -> float
```

Return current health; raises Error if the unit is not visible.

Evaluate a visible camp before choosing where to farm.

Inputs:
- subject: bc.Camp (a valid instance)

```python
result = subject.health()
```

### is_elk

```python
def is_elk(self) -> bool
```

Check whether this camp is an elk.

Evaluate a visible camp before choosing where to farm.

Inputs:
- subject: bc.Camp (a valid instance)

```python
is_elk = subject.is_elk()
```

### is_gem_cluster

```python
def is_gem_cluster(self) -> bool
```

Check whether this camp is a gem cluster.

Evaluate a visible camp before choosing where to farm.

Inputs:
- subject: bc.Camp (a valid instance)

```python
is_gem_cluster = subject.is_gem_cluster()
```

### is_gold_cluster

```python
def is_gold_cluster(self) -> bool
```

Check whether this camp is a gold cluster.

Evaluate a visible camp before choosing where to farm.

Inputs:
- subject: bc.Camp (a valid instance)

```python
is_gold_cluster = subject.is_gold_cluster()
```

### is_monolith

```python
def is_monolith(self) -> bool
```

Check whether this camp is a monolith.

Evaluate a visible camp before choosing where to farm.

Inputs:
- subject: bc.Camp (a valid instance)

```python
is_monolith = subject.is_monolith()
```

### is_visible

```python
def is_visible(self) -> bool
```

Return whether the camp is currently visible.

Evaluate a visible camp before choosing where to farm.

Inputs:
- subject: bc.Camp (a valid instance)

```python
is_visible = subject.is_visible()
```

### is_wolf

```python
def is_wolf(self) -> bool
```

Check whether this camp is a wolf.

Evaluate a visible camp before choosing where to farm.

Inputs:
- subject: bc.Camp (a valid instance)

```python
is_wolf = subject.is_wolf()
```

### kind

```python
def kind(self) -> CampType
```

Return the camp's type.

Evaluate a visible camp before choosing where to farm.

Inputs:
- subject: bc.Camp (a valid instance)

```python
result = subject.kind()
```

### max_health

```python
def max_health(self) -> float
```

Return current maximum health; raises Error if the unit is not visible.

Evaluate a visible camp before choosing where to farm.

Inputs:
- subject: bc.Camp (a valid instance)

```python
result = subject.max_health()
```

### position

```python
def position(self) -> Vec2
```

Return the current tile; raises Error if the unit is not visible.

Evaluate a visible camp before choosing where to farm.

Inputs:
- subject: bc.Camp (a valid instance)

```python
result = subject.position()
```

### spawn_position

```python
def spawn_position(self) -> Vec2
```

Return the camp's spawn tile, not its live position.

Evaluate a visible camp before choosing where to farm.

Inputs:
- subject: bc.Camp (a valid instance)

```python
result = subject.spawn_position()
```

### strength

```python
def strength(self) -> float
```

Return current strength; raises Error if the unit is not visible.

Evaluate a visible camp before choosing where to farm.

Inputs:
- subject: bc.Camp (a valid instance)

```python
result = subject.strength()
```

## cambc.CampType

### to_string

```python
def to_string(value: int) -> str
```



## cambc.Champion

### __eq__

```python
def __eq__(self, other: object) -> bool
```



### __hash__

```python
def __hash__(self) -> int
```



### __index__

```python
def __index__(self) -> int
```



### __repr__

```python
def __repr__(self) -> str
```



### abilities

```python
def abilities(self) -> tuple[Ability, Ability]
```

Return the champion's ability slots.

Evaluate your champion's options during its turn.

```python
subject = bc.me()

result = subject.abilities()
```

### attack

```python
def attack(self, target: Union[Unit, AltarLock]) -> None
```

Basic-attack a visible champion, camp or altar lock in range; requires self. Args: target: Unit or altar lock to attack.

Evaluate your champion's options during its turn.

Inputs:
- target: Union[Unit, AltarLock]

```python
subject = bc.me()

subject.attack(target)
```

### attack_range

```python
def attack_range(self) -> int
```

Return the attack range in Chebyshev tiles; melee champions have range 1.

Evaluate your champion's options during its turn.

```python
subject = bc.me()

result = subject.attack_range()
```

### base_stats

```python
def base_stats(self) -> ChampionStats
```

Return the champion type's design stats.

Evaluate your champion's options during its turn.

```python
subject = bc.me()

result = subject.base_stats()
```

### buy

```python
def buy(self, kind: Union[ItemType, ConsumableType], count: int = 1) -> None
```

Buy count items, or one consumable. Args: kind: Item or consumable to buy. count: Number of items to buy; consumables are bought one at a time.

Evaluate your champion's options during its turn.

Inputs:
- kind: Union[ItemType, ConsumableType]
- count: int

```python
subject = bc.me()

subject.buy(kind, count)
```

### can_attack

```python
def can_attack(self) -> bool
```

Check whether this champion can attack.

Check the action allowance before spending fuel to choose an attack target.

```python
me = bc.me()
action_available = me.can_attack()
```

### can_buy

```python
def can_buy(self, item: Union[ItemType, ConsumableType], count: object = _COUNT_OMITTED) -> bool
```

Return whether the champion can buy an item or consumable in its current state. Args: item: Item or consumable to buy. count: Number of copies to buy.

Evaluate your champion's options during its turn.

Inputs:
- item: Union[ItemType, ConsumableType]
- count: object

```python
subject = bc.me()

can_buy = subject.can_buy(item, count)
```

### can_cast

```python
def can_cast(self) -> bool
```

Check whether this champion can cast.

Check the action allowance before spending fuel to evaluate ready abilities.

```python
me = bc.me()
action_available = me.can_cast()
```

### can_move

```python
def can_move(self) -> bool
```

Check whether this champion can move.

Check the action allowance before spending fuel to plan a path.

```python
me = bc.me()
action_available = me.can_move()
```

### can_sell

```python
def can_sell(self) -> bool
```

Return whether the champion can sell items in its current state.

Evaluate your champion's options during its turn.

```python
subject = bc.me()

can_sell = subject.can_sell()
```

### cancel_recall

```python
def cancel_recall(self) -> None
```

Cancel the current recall; requires self.

Evaluate your champion's options during its turn.

```python
subject = bc.me()

subject.cancel_recall()
```

### cancel_submit_gems

```python
def cancel_submit_gems(self) -> None
```

Cancel the current tribute; requires self.

Evaluate your champion's options during its turn.

```python
subject = bc.me()

subject.cancel_submit_gems()
```

### champion_name

```python
def champion_name(self) -> ChampionType
```

Return the champion's type.

Evaluate your champion's options during its turn.

```python
subject = bc.me()

result = subject.champion_name()
```

### consumables

```python
def consumables(self) -> tuple[Consumable, ...]
```

Consumable slots, indexed by ConsumableType.

Evaluate your champion's options during its turn.

```python
subject = bc.me()

result = subject.consumables()
```

### design

```python
def design(cls, kind: ChampionType) -> Champion
```

Static design of a champion type, as used during the draft. Args: kind: Champion type to describe.

Evaluate your champion's options during its turn.

Inputs:
- kind: ChampionType

```python
subject = bc.me()

result = subject.design(kind)
```

### end_turn

```python
def end_turn(self) -> None
```

End the turn now; requires self.

Evaluate your champion's options during its turn.

```python
subject = bc.me()

subject.end_turn()
```

### focus

```python
def focus(self) -> float
```

Return current focus; raises Error if the unit is not visible.

Evaluate your champion's options during its turn.

```python
subject = bc.me()

result = subject.focus()
```

### gem_count

```python
def gem_count(self) -> int
```

Return the gems the champion is carrying.

Evaluate your champion's options during its turn.

```python
subject = bc.me()

result = subject.gem_count()
```

### gold_count

```python
def gold_count(self) -> int
```

Return the gold the champion is carrying.

Evaluate your champion's options during its turn.

```python
subject = bc.me()

result = subject.gold_count()
```

### has_completed_turn

```python
def has_completed_turn(self) -> bool
```

Check whether this champion has completed its turn.

Evaluate your champion's options during its turn.

```python
subject = bc.me()

has_completed_turn = subject.has_completed_turn()
```

### health

```python
def health(self) -> float
```

Return current health; raises Error if the unit is not visible.

Recall when badly injured and safe from interruption.

Inputs:
- safe_to_recall: your bot's assessment that recalling here is safe and legal

```python
me = bc.me()
if safe_to_recall and me.health() < me.max_health() * 0.3:
    me.recall()
```

### is_alive

```python
def is_alive(self) -> bool
```

Return whether the champion is alive.

Evaluate your champion's options during its turn.

```python
subject = bc.me()

is_alive = subject.is_alive()
```

### is_ally

```python
def is_ally(self) -> bool
```

Check whether this champion belongs to the observing team.

Evaluate your champion's options during its turn.

```python
subject = bc.me()

is_ally = subject.is_ally()
```

### is_enemy

```python
def is_enemy(self) -> bool
```

Check whether this champion belongs to the opposing team.

Evaluate your champion's options during its turn.

```python
subject = bc.me()

is_enemy = subject.is_enemy()
```

### is_recalling

```python
def is_recalling(self) -> bool
```

Check whether this champion is recalling.

Evaluate your champion's options during its turn.

```python
subject = bc.me()

is_recalling = subject.is_recalling()
```

### is_submitting_gems

```python
def is_submitting_gems(self) -> bool
```

Check whether this champion is submitting gems.

Evaluate your champion's options during its turn.

```python
subject = bc.me()

is_submitting_gems = subject.is_submitting_gems()
```

### is_teleporting

```python
def is_teleporting(self) -> bool
```

Check whether this champion is teleporting.

Evaluate your champion's options during its turn.

```python
subject = bc.me()

is_teleporting = subject.is_teleporting()
```

### is_visible

```python
def is_visible(self) -> bool
```

Return whether the champion is currently visible.

Evaluate your champion's options during its turn.

```python
subject = bc.me()

is_visible = subject.is_visible()
```

### item_count

```python
def item_count(self) -> list[int]
```

Carried item counts, indexed by ItemType.

Evaluate your champion's options during its turn.

```python
subject = bc.me()

result = subject.item_count()
```

### max_health

```python
def max_health(self) -> float
```

Return current maximum health; raises Error if the unit is not visible.

Recall when badly injured and safe from interruption.

Inputs:
- safe_to_recall: your bot's assessment that recalling here is safe and legal

```python
me = bc.me()
if safe_to_recall and me.health() < me.max_health() * 0.3:
    me.recall()
```

### move

```python
def move(self, delta: Vec2) -> bool
```

Return False for a newly revealed obstruction; known invalid destinations raise Error. Args: delta: Displacement from the current position.

Take a planned step; false means no movement occurred.

Inputs:
- direction: a legal unit direction, such as east

```python
me = bc.me()
if me.can_move():
    moved = me.move(direction)
```

### move_absolute

```python
def move_absolute(self, destination: Vec2) -> bool
```

Return False for a newly revealed obstruction; known invalid destinations raise Error. Args: destination: Map tile to move to.

Take a planned step; false means no movement occurred.

Inputs:
- destination: a destination selected by your pathfinder

```python
me = bc.me()
if me.can_move():
    moved = me.move_absolute(destination)
```

### move_towards

```python
def move_towards(self, target: Vec2) -> bool
```

Move to the reachable tile on a shortest path to target, avoiding walls, holes, altars, the enemy spawn and visible units. Return False without moving when already there, unable to move, or target is blocked or unreachable, and for a newly revealed obstruction. Args: target: Map tile to approach.

Take a planned step; false means no movement occurred.

Inputs:
- destination: a destination selected by your pathfinder

```python
me = bc.me()
if me.can_move():
    moved = me.move_towards(destination)
```

### passive

```python
def passive(self) -> PassiveType
```

Return the champion's passive.

Evaluate your champion's options during its turn.

```python
subject = bc.me()

result = subject.passive()
```

### place_ward

```python
def place_ward(self, destination: Vec2) -> bool
```

Return False for a newly revealed obstruction; known invalid destinations raise Error. Args: destination: Tile to place the ward on.

Evaluate your champion's options during its turn.

Inputs:
- destination: Vec2

```python
subject = bc.me()

result = subject.place_ward(destination)
```

### position

```python
def position(self) -> Vec2
```

Return the current tile; raises Error if the unit is not visible.

Evaluate your champion's options during its turn.

```python
subject = bc.me()

result = subject.position()
```

### prev_priority

```python
def prev_priority(self) -> int
```

Return the priority used for the current round.

Evaluate your champion's options during its turn.

```python
subject = bc.me()

result = subject.prev_priority()
```

### priority

```python
def priority(self) -> int
```

Return the priority that will apply from the next round.

Evaluate your champion's options during its turn.

```python
subject = bc.me()

result = subject.priority()
```

### recall

```python
def recall(self) -> None
```

Start channelling a recall to the team spawn; requires self.

Recall when badly injured and safe from interruption.

Inputs:
- safe_to_recall: your bot's assessment that recalling here is safe and legal

```python
me = bc.me()
if safe_to_recall and me.health() < me.max_health() * 0.3:
    me.recall()
```

### remaining_channel_time

```python
def remaining_channel_time(self) -> int
```

Return the rounds left on the current recall, tribute or teleport channel.

Evaluate your champion's options during its turn.

```python
subject = bc.me()

result = subject.remaining_channel_time()
```

### restrictions

```python
def restrictions(self) -> BuffRestrictions
```

Return the actions the champion's buffs currently prohibit.

Evaluate your champion's options during its turn.

```python
subject = bc.me()

result = subject.restrictions()
```

### sell

```python
def sell(self, kind: ItemType, count: int = 1) -> None
```

Sell items; requires self and the engine validates location and inventory. Args: kind: Item to sell. count: Number of copies to sell.

Evaluate your champion's options during its turn.

Inputs:
- kind: ItemType
- count: int

```python
subject = bc.me()

subject.sell(kind, count)
```

### set_priority

```python
def set_priority(self, priority: int) -> None
```

Set the champion's scheduling priority; requires self. Args: priority: New priority; takes effect from the next round and persists.

Evaluate your champion's options during its turn.

Inputs:
- priority: int

```python
subject = bc.me()

subject.set_priority(priority)
```

### state

```python
def state(self) -> ChampionState
```

Return the champion's life, channel and action flags.

Evaluate your champion's options during its turn.

```python
subject = bc.me()

result = subject.state()
```

### strength

```python
def strength(self) -> float
```

Return current strength; raises Error if the unit is not visible.

Evaluate your champion's options during its turn.

```python
subject = bc.me()

result = subject.strength()
```

### submit_gems

```python
def submit_gems(self, altar: Vec2) -> None
```

Start tributing carried gems at an altar; requires self. Args: altar: Altar tile to tribute at.

Evaluate your champion's options during its turn.

Inputs:
- altar: Vec2

```python
subject = bc.me()

subject.submit_gems(altar)
```

### team

```python
def team(self) -> Team
```

Return the champion's team.

Evaluate your champion's options during its turn.

```python
subject = bc.me()

result = subject.team()
```

### visible_tiles

```python
def visible_tiles(self) -> Bitboard
```

Current vision for this champion.

Evaluate your champion's options during its turn.

```python
subject = bc.me()

result = subject.visible_tiles()
```

### visible_tiles_from

```python
def visible_tiles_from(self, position: Vec2) -> Bitboard
```

Vision this champion would have at position. Args: position: Hypothetical tile to see from.

Evaluate your champion's options during its turn.

Inputs:
- position: Vec2

```python
subject = bc.me()

result = subject.visible_tiles_from(position)
```

### visible_tiles_from_into

```python
def visible_tiles_from_into(self, position: Vec2, out: Bitboard) -> None
```

Like visible_tiles_from, but writes into out. Args: position: Hypothetical tile to see from. out: Destination Bitboard; its previous contents are overwritten.

Evaluate your champion's options during its turn.

Inputs:
- position: Vec2
- out: Bitboard

```python
subject = bc.me()

subject.visible_tiles_from_into(position, out)
```

### visible_tiles_into

```python
def visible_tiles_into(self, out: Bitboard) -> None
```

Like visible_tiles, but writes into out. Args: out: Destination Bitboard; its previous contents are overwritten.

Evaluate your champion's options during its turn.

Inputs:
- out: Bitboard

```python
subject = bc.me()

subject.visible_tiles_into(out)
```

### ward_cooldown

```python
def ward_cooldown(self) -> int
```

Return the rounds until another ward can be placed.

Evaluate your champion's options during its turn.

```python
subject = bc.me()

result = subject.ward_cooldown()
```

### ward_placement_tiles

```python
def ward_placement_tiles(self) -> Bitboard
```

Return the tiles where this champion could place a ward now.

Evaluate your champion's options during its turn.

```python
subject = bc.me()

result = subject.ward_placement_tiles()
```

### ward_placement_tiles_into

```python
def ward_placement_tiles_into(self, out: Bitboard) -> None
```

Like ward_placement_tiles, but writes into out. Args: out: Destination Bitboard; its previous contents are overwritten.

Evaluate your champion's options during its turn.

Inputs:
- out: Bitboard

```python
subject = bc.me()

subject.ward_placement_tiles_into(out)
```

### ward_positions

```python
def ward_positions(self) -> list[Vec2]
```

Return the tiles of this champion's placed wards.

Evaluate your champion's options during its turn.

```python
subject = bc.me()

result = subject.ward_positions()
```

## cambc.ChampionDraft

### to_string

```python
def to_string(value: int) -> str
```



## cambc.ChampionState

### __and__

```python
def __and__(self, other: int) -> Self
```



Combine or inspect flags before deciding which actions or targets are allowed.

Inputs:
- other: int

```python
subject = bc.me().state()

result = subject & other
```

### __contains__

```python
def __contains__(self, flags: Self) -> bool
```



Combine or inspect flags before deciding which actions or targets are allowed.

Inputs:
- flags: Self

```python
subject = bc.me().state()

result = flags in subject
```

### __invert__

```python
def __invert__(self) -> Self
```



Combine or inspect flags before deciding which actions or targets are allowed.

```python
subject = bc.me().state()

result = ~subject
```

### __iter__

```python
def __iter__(self) -> Iterator[Self]
```



Combine or inspect flags before deciding which actions or targets are allowed.

```python
subject = bc.me().state()

result = iter(subject)
```

### __or__

```python
def __or__(self, other: int) -> Self
```



Combine or inspect flags before deciding which actions or targets are allowed.

Inputs:
- other: int

```python
subject = bc.me().state()

result = subject | other
```

### __rand__

```python
def __rand__(self, other: int) -> Self
```



Combine or inspect flags before deciding which actions or targets are allowed.

Inputs:
- other: int

```python
subject = bc.me().state()

result = subject.__rand__(other)
```

### __ror__

```python
def __ror__(self, other: int) -> Self
```



Combine or inspect flags before deciding which actions or targets are allowed.

Inputs:
- other: int

```python
subject = bc.me().state()

result = subject.__ror__(other)
```

### __rsub__

```python
def __rsub__(self, other: int) -> Self
```



Combine or inspect flags before deciding which actions or targets are allowed.

Inputs:
- other: int

```python
subject = bc.me().state()

result = subject.__rsub__(other)
```

### __rxor__

```python
def __rxor__(self, other: int) -> Self
```



Combine or inspect flags before deciding which actions or targets are allowed.

Inputs:
- other: int

```python
subject = bc.me().state()

result = subject.__rxor__(other)
```

### __sub__

```python
def __sub__(self, other: int) -> Self
```



Combine or inspect flags before deciding which actions or targets are allowed.

Inputs:
- other: int

```python
subject = bc.me().state()

result = subject - other
```

### __xor__

```python
def __xor__(self, other: int) -> Self
```



Combine or inspect flags before deciding which actions or targets are allowed.

Inputs:
- other: int

```python
subject = bc.me().state()

result = subject ^ other
```

### all

```python
def all(cls) -> Self
```

Return a set with every named flag.

Combine or inspect flags before deciding which actions or targets are allowed.

```python
subject = bc.me().state()

result = subject.all()
```

### empty

```python
def empty(cls) -> Self
```

Return a set with no flags.

Combine or inspect flags before deciding which actions or targets are allowed.

```python
subject = bc.me().state()

result = subject.empty()
```

### from_bits

```python
def from_bits(cls, bits: int) -> Optional[Self]
```

Return the set for raw bits, or None if any bit is not a named flag. Args: bits: Raw flag bits.

Combine or inspect flags before deciding which actions or targets are allowed.

Inputs:
- bits: int

```python
subject = bc.me().state()

result = subject.from_bits(bits)
```

### from_bits_truncate

```python
def from_bits_truncate(cls, bits: int) -> Self
```

Return the set for raw bits, dropping bits that are not named flags. Args: bits: Raw flag bits.

Combine or inspect flags before deciding which actions or targets are allowed.

Inputs:
- bits: int

```python
subject = bc.me().state()

result = subject.from_bits_truncate(bits)
```

### intersects

```python
def intersects(self, flags: Self) -> bool
```

Return whether this set shares any flag with flags. Args: flags: Flags to test.

Combine or inspect flags before deciding which actions or targets are allowed.

Inputs:
- flags: Self

```python
subject = bc.me().state()

result = subject.intersects(flags)
```

### is_all

```python
def is_all(self) -> bool
```

Return whether every named flag is set.

Combine or inspect flags before deciding which actions or targets are allowed.

```python
subject = bc.me().state()

is_all = subject.is_all()
```

### is_dead

```python
def is_dead(self) -> bool
```



Combine or inspect flags before deciding which actions or targets are allowed.

```python
subject = bc.me().state()

is_dead = subject.is_dead()
```

## cambc.ChampionType

### to_string

```python
def to_string(value: int) -> str
```



## cambc.Consumable

### __eq__

```python
def __eq__(self, other: object) -> bool
```



### __hash__

```python
def __hash__(self) -> int
```



### __init__

```python
def __init__(self) -> None
```



This view cannot be constructed directly. Obtain it from the SDK when inspecting the current turn or map.

```python
consumables = bc.me().consumables()
```

### __repr__

```python
def __repr__(self) -> str
```



### count

```python
def count(self) -> int
```

Return how many the champion is carrying.

Plan a purchase or use an owned consumable.

Inputs:
- subject: bc.Consumable (a valid instance)

```python
result = subject.count()
```

### kind

```python
def kind(self) -> ConsumableType
```

Return the consumable's type.

Plan a purchase or use an owned consumable.

Inputs:
- subject: bc.Consumable (a valid instance)

```python
result = subject.kind()
```

### use

```python
def use(self, destination: Optional[Vec2] = None) -> bool
```

Return False for a newly revealed obstruction; known invalid destinations raise Error. Args: destination: Tile to use the consumable at.

Plan a purchase or use an owned consumable.

Inputs:
- subject: bc.Consumable (a valid instance)
- destination: Optional[Vec2]

```python
result = subject.use(destination)
```

## cambc.ConsumableType

### __new__

```python
def __new__(cls, value: int) -> ConsumableType
```



Plan a purchase or use an owned consumable.

Inputs:
- value: int

```python
result = bc.ConsumableType(value)
```

### __repr__

```python
def __repr__(self) -> str
```



### carry_limit

```python
def carry_limit(self) -> int
```

Return how many a champion can carry at once.

Plan a purchase or use an owned consumable.

Inputs:
- subject: bc.ConsumableType (a valid instance)

```python
result = subject.carry_limit()
```

### cost

```python
def cost(self) -> int
```

Return the gold cost to buy one.

Plan a purchase or use an owned consumable.

Inputs:
- subject: bc.ConsumableType (a valid instance)

```python
result = subject.cost()
```

### info

```python
def info(self) -> ConsumableInfo
```

Return the consumable's static design data.

Plan a purchase or use an owned consumable.

Inputs:
- subject: bc.ConsumableType (a valid instance)

```python
result = subject.info()
```

### name

```python
def name(self) -> str
```

Return the consumable's display name.

Plan a purchase or use an owned consumable.

Inputs:
- subject: bc.ConsumableType (a valid instance)

```python
result = subject.name
```

## cambc.debug

### draw_dot

```python
def draw_dot(position: Vec2, rgb: int) -> None
```

Draw a debug dot in the replay. Args: position: Tile to mark. rgb: Packed 0xRRGGBB colour.

Mark a decision in your replay debug overlay to understand the bot's route or target.

Inputs:
- position: Vec2
- rgb: int

```python
bc.debug.draw_dot(position, rgb)
```

### draw_line

```python
def draw_line(start: Vec2, end: Vec2, rgb: int) -> None
```

Draw a debug line in the replay. Args: start: Start tile. end: End tile. rgb: Packed 0xRRGGBB colour.

Mark a decision in your replay debug overlay to understand the bot's route or target.

Inputs:
- start: Vec2
- end: Vec2
- rgb: int

```python
bc.debug.draw_line(start, end, rgb)
```

## cambc.DistanceField

### __eq__

```python
def __eq__(self, other: object) -> bool
```



### __init__

```python
def __init__(self) -> None
```



Choose a route around blocked tiles.

```python
result = bc.DistanceField()
```

### compute

```python
def compute(self, walls: Bitboard, roots: Bitboard, visited: Bitboard, max_distance: int = ...) -> None
```

Compute distances from roots around walls into this field. Args: walls: Impassable tiles. roots: Tiles at distance zero. visited: Receives the tiles the search reached. max_distance: Tiles farther than this are left unreached.

Find a step towards the goal tiles. The result is a direction for move.

Inputs:
- blocked: impassable/occupied tiles, excluding your own tile
- goals: legal destination tiles

```python
field = bc.DistanceField()
field.compute(blocked, goals, bc.Bitboard())
direction = field.next_move_from(bc.me().position())
```

### compute_to

```python
def compute_to( self, walls: Bitboard, roots: Bitboard, destinations: Bitboard, visited: Bitboard, max_distance: int = ... ) -> None
```

Compute distances from roots until destinations are reached or the search is exhausted. Args: walls: Impassable tiles. roots: Tiles at distance zero. destinations: The search stops once these tiles are reached. visited: Receives the tiles the search reached. max_distance: Tiles farther than this are left unreached.

Choose a route around blocked tiles.

Inputs:
- walls: Bitboard
- roots: Bitboard
- destinations: Bitboard
- visited: Bitboard
- max_distance: int

```python
bc.DistanceField.compute_to(walls, roots, destinations, visited, max_distance)
```

### compute_to_with_expansion_count

```python
def compute_to_with_expansion_count( self, walls: Bitboard, roots: Bitboard, destinations: Bitboard, visited: Bitboard, max_distance: int = ... ) -> int
```

Like compute_to, but return the number of tiles the search expanded. Args: walls: Impassable tiles. roots: Tiles at distance zero. destinations: The search stops once these tiles are reached. visited: Receives the tiles the search reached. max_distance: Tiles farther than this are left unreached.

Choose a route around blocked tiles.

Inputs:
- walls: Bitboard
- roots: Bitboard
- destinations: Bitboard
- visited: Bitboard
- max_distance: int

```python
result = bc.DistanceField.compute_to_with_expansion_count(walls, roots, destinations, visited, max_distance)
```

### compute_with_expansion_count

```python
def compute_with_expansion_count( self, walls: Bitboard, roots: Bitboard, visited: Bitboard, max_distance: int = ... ) -> int
```

Like compute, but return the number of tiles the search expanded. Args: walls: Impassable tiles. roots: Tiles at distance zero. visited: Receives the tiles the search reached. max_distance: Tiles farther than this are left unreached.

Choose a route around blocked tiles.

Inputs:
- walls: Bitboard
- roots: Bitboard
- visited: Bitboard
- max_distance: int

```python
result = bc.DistanceField.compute_with_expansion_count(walls, roots, visited, max_distance)
```

### copy

```python
def copy(self) -> DistanceField
```

Return an independent copy.

Choose a route around blocked tiles.

Inputs:
- subject: bc.DistanceField (a valid instance)

```python
result = subject.copy()
```

### export_linear_buffer

```python
def export_linear_buffer(self) -> bytes
```

Return the contents as a row-major buffer with one value per tile.

Choose a route around blocked tiles.

Inputs:
- subject: bc.DistanceField (a valid instance)

```python
result = subject.export_linear_buffer()
```

### export_linear_buffer_into

```python
def export_linear_buffer_into(self, out: Buffer) -> None
```

Write the contents as a row-major buffer with one value per tile. Args: out: Writable bytes-like object exactly linear_buffer_size() long.

Choose a route around blocked tiles.

Inputs:
- subject: bc.DistanceField (a valid instance)
- out: Buffer

```python
subject.export_linear_buffer_into(out)
```

### export_raw_buffer

```python
def export_raw_buffer(self) -> bytes
```

Return the contents as an engine-chunked buffer.

Choose a route around blocked tiles.

Inputs:
- subject: bc.DistanceField (a valid instance)

```python
result = subject.export_raw_buffer()
```

### export_raw_buffer_into

```python
def export_raw_buffer_into(self, out: Buffer) -> None
```

Write the contents as an engine-chunked buffer. Args: out: Writable bytes-like object exactly raw_buffer_size() long.

Choose a route around blocked tiles.

Inputs:
- subject: bc.DistanceField (a valid instance)
- out: Buffer

```python
subject.export_raw_buffer_into(out)
```

### get

```python
def get(self, position: Vec2) -> int
```

Return the distance stored at a tile; raises Error outside the map. Args: position: Tile to query.

Choose a route around blocked tiles.

Inputs:
- subject: bc.DistanceField (a valid instance)
- position: Vec2

```python
result = subject.get(position)
```

### height

```python
def height(self) -> int
```

Return the map height in tiles.

### import_linear_buffer

```python
def import_linear_buffer(self, data: Buffer) -> None
```

Replace the contents from a row-major buffer with one value per tile. Args: data: Bytes-like object exactly linear_buffer_size() long.

Choose a route around blocked tiles.

Inputs:
- subject: bc.DistanceField (a valid instance)
- data: Buffer

```python
subject.import_linear_buffer(data)
```

### import_raw_buffer

```python
def import_raw_buffer(self, data: Buffer) -> None
```

Replace the contents from an engine-chunked buffer. Args: data: Bytes-like object exactly raw_buffer_size() long.

Choose a route around blocked tiles.

Inputs:
- subject: bc.DistanceField (a valid instance)
- data: Buffer

```python
subject.import_raw_buffer(data)
```

### linear_buffer_size

```python
def linear_buffer_size() -> int
```

Return the size in bytes of the row-major buffer.

Choose a route around blocked tiles.

```python
result = bc.DistanceField.linear_buffer_size()
```

### next_move_from

```python
def next_move_from(self, position: Vec2) -> Optional[Vec2]
```

Return the first optimal step towards a root as a direction delta, or None at a root or unreached tile. Args: position: Tile to step from.

Find a step towards the goal tiles. The result is a direction for move.

Inputs:
- blocked: impassable/occupied tiles, excluding your own tile
- goals: legal destination tiles

```python
field = bc.DistanceField()
field.compute(blocked, goals, bc.Bitboard())
direction = field.next_move_from(bc.me().position())
```

### next_moves_from

```python
def next_moves_from(self, position: Vec2) -> list[Vec2]
```

Return every optimal step towards a root as direction deltas, in compass order from north. Args: position: Tile to step from.

Choose a route around blocked tiles.

Inputs:
- subject: bc.DistanceField (a valid instance)
- position: Vec2

```python
result = subject.next_moves_from(position)
```

### print

```python
def print(self) -> None
```

Print this board to stdout for debugging.

Choose a route around blocked tiles.

Inputs:
- subject: bc.DistanceField (a valid instance)

```python
subject.print()
```

### raw_buffer_size

```python
def raw_buffer_size() -> int
```

Return the size in bytes of the engine-chunked buffer.

Choose a route around blocked tiles.

```python
result = bc.DistanceField.raw_buffer_size()
```

### set

```python
def set(self, position: Vec2, value: int) -> None
```

Store a distance at a tile; raises Error outside the map. Args: position: Tile to update. value: Distance to store.

Choose a route around blocked tiles.

Inputs:
- subject: bc.DistanceField (a valid instance)
- position: Vec2
- value: int

```python
subject.set(position, value)
```

### width

```python
def width(self) -> int
```

Return the map width in tiles.

## cambc.draft

### current_draft

```python
def current_draft(team: Team) -> list[ChampionDraft]
```

Picks a team has made so far, in order. Args: team: Team whose picks to return.

Choose your team's roster during the draft phase.

Inputs:
- team: Team

```python
result = bc.draft.current_draft(team)
```

### pick

```python
def pick(champion: ChampionDraft) -> None
```

Pick a champion for the current draft round; only valid during the draft. Args: champion: Champion to pick.

Choose your team's roster during the draft phase.

Inputs:
- champion: ChampionDraft

```python
bc.draft.pick(champion)
```

### team_size

```python
def team_size() -> int
```

Champions each team drafts.

Choose your team's roster during the draft phase.

```python
result = bc.draft.team_size()
```

## cambc.DraftMemoryBuffer

### __bytes__

```python
def __bytes__(self) -> bytes
```



Pass your drafting decisions to the bot's later turns using draft memory.

Inputs:
- subject: bc.DraftMemoryBuffer (a valid instance)

```python
result = bytes(subject)
```

### __getitem__

```python
def __getitem__(self, offset: int) -> int
```



Pass your drafting decisions to the bot's later turns using draft memory.

Inputs:
- subject: bc.DraftMemoryBuffer (a valid instance)
- offset: int

```python
result = subject[offset]
```

### __init__

```python
def __init__(self) -> None
```



Pass your drafting decisions to the bot's later turns using draft memory.

```python
result = bc.DraftMemoryBuffer()
```

### __iter__

```python
def __iter__(self) -> Iterator[int]
```



Pass your drafting decisions to the bot's later turns using draft memory.

Inputs:
- subject: bc.DraftMemoryBuffer (a valid instance)

```python
result = iter(subject)
```

### __len__

```python
def __len__(self) -> int
```



### is_empty

```python
def is_empty(self) -> bool
```

Return whether no draft memory was submitted.

Pass your drafting decisions to the bot's later turns using draft memory.

Inputs:
- subject: bc.DraftMemoryBuffer (a valid instance)

```python
is_empty = subject.is_empty()
```

### submit

```python
def submit(self, data: Union[bytes, bytearray, memoryview, DraftMemoryBuffer]) -> None
```

Submit bytes-like data as the next draft memory. Args: data: Bytes-like object to pass to this team's gameplay bots.

Pass your drafting decisions to the bot's later turns using draft memory.

Inputs:
- subject: bc.DraftMemoryBuffer (a valid instance)
- data: Union[bytes, bytearray, memoryview, DraftMemoryBuffer]

```python
subject.submit(data)
```

## cambc.Error

### __init__

```python
def __init__(self, code: int, message: str = "") -> None
```



Inspect a caught SDK error when diagnosing a rejected action.

Inputs:
- code: int
- message: str

```python
result = bc.Error(code, message)
```

### __str__

```python
def __str__(self) -> str
```



## cambc.ErrorCode

### to_string

```python
def to_string(value: int) -> str
```



## cambc.game_map

### altars

```python
def altars() -> Bitboard
```

Return the altar tiles, where gems are tributed.

Build a terrain-only walking mask. Also exclude occupied tiles and the enemy spawn when selecting a legal step.

```python
blocked = bc.game_map.walls() | bc.game_map.holes() | bc.game_map.altars()
walkable = ~blocked
```

### bushes

```python
def bushes() -> Bitboard
```

Return the bush tiles, which hide champions from outside vision.

Inspect map geometry when choosing a route or objective.

```python
result = bc.game_map.bushes()
```

### camp

```python
def camp(position: Vec2) -> Camp
```

The camp that spawns at position; IndexError if none does. Args: position: Spawn tile of the camp.

Inspect map geometry when choosing a route or objective.

Inputs:
- position: Vec2

```python
result = bc.game_map.camp(position)
```

### camp_groups

```python
def camp_groups() -> tuple[CampGroup, ...]
```

Camp groups, also available during the draft.

Inspect map geometry when choosing a route or objective.

```python
result = bc.game_map.camp_groups()
```

### height

```python
def height() -> int
```

Return the map height in tiles.

### holes

```python
def holes() -> Bitboard
```

Return the hole tiles, which block movement but not vision.

Build a terrain-only walking mask. Also exclude occupied tiles and the enemy spawn when selecting a legal step.

```python
blocked = bc.game_map.walls() | bc.game_map.holes() | bc.game_map.altars()
walkable = ~blocked
```

### is_in_bounds

```python
def is_in_bounds(position: Vec2) -> bool
```

Return whether a position lies on the map. Args: position: Position to check.

Inspect map geometry when choosing a route or objective.

Inputs:
- position: Vec2

```python
is_in_bounds = bc.game_map.is_in_bounds(position)
```

### reflect_horizontal

```python
def reflect_horizontal(position: Vec2) -> Vec2
```

Return a position reflected across the map horizontally, reversing x. Args: position: Map position to reflect.

Inspect map geometry when choosing a route or objective.

Inputs:
- position: Vec2

```python
result = bc.game_map.reflect_horizontal(position)
```

### reflect_vertical

```python
def reflect_vertical(position: Vec2) -> Vec2
```

Return a position reflected across the map vertically, reversing y. Args: position: Map position to reflect.

Inspect map geometry when choosing a route or objective.

Inputs:
- position: Vec2

```python
result = bc.game_map.reflect_vertical(position)
```

### rotate_180

```python
def rotate_180(position: Vec2) -> Vec2
```

Return a position rotated 180 degrees within the map. Args: position: Map position to rotate.

Inspect map geometry when choosing a route or objective.

Inputs:
- position: Vec2

```python
result = bc.game_map.rotate_180(position)
```

### spawn_region

```python
def spawn_region(team: Team) -> Bitboard
```

Return a team's spawn region. Args: team: Team whose spawn region to return.

Inspect map geometry when choosing a route or objective.

Inputs:
- team: Team

```python
result = bc.game_map.spawn_region(team)
```

### symmetry

```python
def symmetry() -> Symmetry
```

Return the symmetry the map was generated with.

Inspect map geometry when choosing a route or objective.

```python
result = bc.game_map.symmetry()
```

### walls

```python
def walls() -> Bitboard
```

Cached wall mask; copy() before mutating.

Build a terrain-only walking mask. Also exclude occupied tiles and the enemy spawn when selecting a legal step.

```python
blocked = bc.game_map.walls() | bc.game_map.holes() | bc.game_map.altars()
walkable = ~blocked
```

### width

```python
def width() -> int
```

Return the map width in tiles.

## cambc.game_map.CampGroup

### __eq__

```python
def __eq__(self, other: object) -> bool
```



### __hash__

```python
def __hash__(self) -> int
```



### __index__

```python
def __index__(self) -> int
```



### __init__

```python
def __init__(self) -> None
```



This view cannot be constructed directly. Obtain it from the SDK when inspecting the current turn or map.

```python
groups = bc.game_map.camp_groups()
```

### __iter__

```python
def __iter__(self) -> Iterator[Camp]
```



Evaluate a visible camp before choosing where to farm.

Inputs:
- subject: bc.game_map.CampGroup (a valid instance)

```python
result = iter(subject)
```

### __len__

```python
def __len__(self) -> int
```



### camps

```python
def camps(self) -> tuple[Camp, ...]
```

Return the camps in the group.

Evaluate a visible camp before choosing where to farm.

Inputs:
- subject: bc.game_map.CampGroup (a valid instance)

```python
result = subject.camps()
```

### gem_value

```python
def gem_value(self) -> int
```

Return the gems awarded for clearing the group.

Evaluate a visible camp before choosing where to farm.

Inputs:
- subject: bc.game_map.CampGroup (a valid instance)

```python
result = subject.gem_value()
```

### gold_value

```python
def gold_value(self) -> int
```

Return the gold awarded for clearing the group.

Evaluate a visible camp before choosing where to farm.

Inputs:
- subject: bc.game_map.CampGroup (a valid instance)

```python
result = subject.gold_value()
```

### max_respawn_timer

```python
def max_respawn_timer(self) -> int
```

Return the number of rounds the group takes to respawn after being cleared.

Evaluate a visible camp before choosing where to farm.

Inputs:
- subject: bc.game_map.CampGroup (a valid instance)

```python
result = subject.max_respawn_timer()
```

### spawn_tiles

```python
def spawn_tiles(self) -> Bitboard
```

Return the spawn tiles of the group's camps.

Evaluate a visible camp before choosing where to farm.

Inputs:
- subject: bc.game_map.CampGroup (a valid instance)

```python
result = subject.spawn_tiles()
```

### spawn_tiles_into

```python
def spawn_tiles_into(self, out: Bitboard) -> None
```

Like spawn_tiles, but writes into out. Args: out: Destination Bitboard; its previous contents are overwritten.

Evaluate a visible camp before choosing where to farm.

Inputs:
- subject: bc.game_map.CampGroup (a valid instance)
- out: Bitboard

```python
subject.spawn_tiles_into(out)
```

### state

```python
def state(self) -> CampGroupState
```

Return the group's current state.

Evaluate a visible camp before choosing where to farm.

Inputs:
- subject: bc.game_map.CampGroup (a valid instance)

```python
result = subject.state()
```

## cambc.ItemPassive

### to_string

```python
def to_string(value: int) -> str
```



## cambc.ItemType

### __new__

```python
def __new__(cls, value: int) -> ItemType
```



Plan a purchase or use an owned consumable.

Inputs:
- value: int

```python
result = bc.ItemType(value)
```

### __repr__

```python
def __repr__(self) -> str
```



### combine_count

```python
def combine_count(self) -> int
```

Return how many copies combine into the result item.

Plan a purchase or use an owned consumable.

Inputs:
- subject: bc.ItemType (a valid instance)

```python
result = subject.combine_count()
```

### cost

```python
def cost(self) -> int
```

Return the gold cost to buy the item.

Plan a purchase or use an owned consumable.

Inputs:
- subject: bc.ItemType (a valid instance)

```python
result = subject.cost()
```

### focus_points

```python
def focus_points(self) -> int
```

Return the focus the item grants.

Plan a purchase or use an owned consumable.

Inputs:
- subject: bc.ItemType (a valid instance)

```python
result = subject.focus_points()
```

### health_points

```python
def health_points(self) -> int
```

Return the maximum health the item grants.

Plan a purchase or use an owned consumable.

Inputs:
- subject: bc.ItemType (a valid instance)

```python
result = subject.health_points()
```

### info

```python
def info(self) -> ItemInfo
```

Return the item's static design data.

Plan a purchase or use an owned consumable.

Inputs:
- subject: bc.ItemType (a valid instance)

```python
result = subject.info()
```

### is_purchasable

```python
def is_purchasable(self) -> bool
```

Return whether the item can be bought directly from the shop.

Plan a purchase or use an owned consumable.

Inputs:
- subject: bc.ItemType (a valid instance)

```python
is_purchasable = subject.is_purchasable()
```

### name

```python
def name(self) -> str
```

Return the item's display name.

Plan a purchase or use an owned consumable.

Inputs:
- subject: bc.ItemType (a valid instance)

```python
result = subject.name
```

### passive

```python
def passive(self) -> Optional[ItemPassive]
```

Return the passive effect the item grants.

Plan a purchase or use an owned consumable.

Inputs:
- subject: bc.ItemType (a valid instance)

```python
result = subject.passive()
```

### passive_magnitude

```python
def passive_magnitude(self) -> float
```

Return the strength of the item's passive effect.

Plan a purchase or use an owned consumable.

Inputs:
- subject: bc.ItemType (a valid instance)

```python
result = subject.passive_magnitude()
```

### result

```python
def result(self) -> Optional[ItemType]
```

Return the item these copies combine into, or None if it does not combine.

Plan a purchase or use an owned consumable.

Inputs:
- subject: bc.ItemType (a valid instance)

```python
result = subject.result()
```

### strength_points

```python
def strength_points(self) -> int
```

Return the strength the item grants.

Plan a purchase or use an owned consumable.

Inputs:
- subject: bc.ItemType (a valid instance)

```python
result = subject.strength_points()
```

## cambc.PassiveType

### to_string

```python
def to_string(value: int) -> str
```



## cambc.SharedMemoryBuffer

### __getitem__

```python
def __getitem__(self, offset: int) -> int
```



Share an objective using your team's agreed memory layout.

Inputs:
- subject: bc.SharedMemoryBuffer (a valid instance)
- offset: int

```python
result = subject[offset]
```

### __len__

```python
def __len__(self) -> int
```



### __setitem__

```python
def __setitem__(self, offset: int, value: int) -> None
```



Share an objective using your team's agreed memory layout.

Inputs:
- subject: bc.SharedMemoryBuffer (a valid instance)
- offset: int
- value: int

```python
subject[offset] = value
```

### read

```python
def read(self, offset: int, out: Union[bytearray, memoryview]) -> None
```

Fill a writable bytes-like object from offset. Args: offset: Byte offset into shared memory. out: Writable bytes-like object; its length sets how many bytes are read.

Reserve byte zero in your team's memory layout for a shared objective ID. All allied bots must agree on its meaning.

```python
data = bytearray(1)
bc.shared_memory.read(0, data)
objective_id = data[0]
```

### size

```python
def size() -> int
```

Return the shared memory size in bytes.

### write

```python
def write(self, offset: int, data: Union[bytes, bytearray, memoryview]) -> None
```

Write a bytes-like object starting at offset. Args: offset: Byte offset into shared memory. data: Bytes-like object to write.

Reserve byte zero in your team's memory layout for a shared objective ID. All allied bots must agree on its meaning.

```python
bc.shared_memory.write(0, bytes([2]))  # Agree to focus objective 2.
```

## cambc.Symmetry

### to_string

```python
def to_string(value: int) -> str
```



## cambc.Team

### opponent

```python
def opponent(team: int) -> int
```



Use this value in your bot's draft or turn logic.

Inputs:
- team: int

```python
result = bc.Team.opponent(team)
```

### opponent

```python
def opponent(team: Team) -> Team
```



Use this value in your bot's draft or turn logic.

Inputs:
- team: Team

```python
result = bc.Team.opponent(team)
```

### to_string

```python
def to_string(value: int) -> str
```



## cambc.Teleport

### champion

```python
def champion(self) -> Champion
```

Return the champion channelling the teleport.

Check visible objects before choosing a destination.

Inputs:
- subject: bc.Teleport (a valid instance)

```python
result = subject.champion()
```

### is_ally

```python
def is_ally(self) -> bool
```

Check whether this teleport belongs to the observing team.

Check visible objects before choosing a destination.

Inputs:
- subject: bc.Teleport (a valid instance)

```python
is_ally = subject.is_ally()
```

### is_enemy

```python
def is_enemy(self) -> bool
```

Check whether this teleport belongs to the opposing team.

Check visible objects before choosing a destination.

Inputs:
- subject: bc.Teleport (a valid instance)

```python
is_enemy = subject.is_enemy()
```

### position

```python
def position(self) -> Vec2
```

Return the reserved destination tile.

Check visible objects before choosing a destination.

Inputs:
- subject: bc.Teleport (a valid instance)

```python
result = subject.position()
```

### remaining_time

```python
def remaining_time(self) -> int
```

Return the rounds left before the teleport completes.

Check visible objects before choosing a destination.

Inputs:
- subject: bc.Teleport (a valid instance)

```python
result = subject.remaining_time()
```

### team

```python
def team(self) -> Team
```

Return the team of the teleporting champion.

Check visible objects before choosing a destination.

Inputs:
- subject: bc.Teleport (a valid instance)

```python
result = subject.team()
```

### visible_tiles

```python
def visible_tiles(self) -> Bitboard
```

Return the tiles visible from the reservation.

Check visible objects before choosing a destination.

Inputs:
- subject: bc.Teleport (a valid instance)

```python
result = subject.visible_tiles()
```

### visible_tiles_into

```python
def visible_tiles_into(self, out: Bitboard) -> None
```

Like visible_tiles, but writes into out. Args: out: Destination Bitboard; its previous contents are overwritten.

Check visible objects before choosing a destination.

Inputs:
- subject: bc.Teleport (a valid instance)
- out: Bitboard

```python
subject.visible_tiles_into(out)
```

## cambc.Unit

### __eq__

```python
def __eq__(self, other: object) -> bool
```



### __hash__

```python
def __hash__(self) -> int
```



### __init__

```python
def __init__(self) -> None
```



This view cannot be constructed directly. Obtain it from the SDK when inspecting the current turn or map.

```python
unit = bc.me()
```

### attack_range

```python
def attack_range(self) -> int
```

Return the attack range in Chebyshev tiles; melee units have range 1.

Evaluate your champion's options during its turn.

```python
subject = bc.me()

result = subject.attack_range()
```

### attack_tiles

```python
def attack_tiles(self) -> Bitboard
```

Return the tiles within attack range of the unit's current position.

Evaluate your champion's options during its turn.

```python
subject = bc.me()

result = subject.attack_tiles()
```

### attack_tiles_into

```python
def attack_tiles_into(self, out: Bitboard) -> None
```

Like attack_tiles, but writes into out. Args: out: Destination Bitboard; its previous contents are overwritten.

Evaluate your champion's options during its turn.

Inputs:
- out: Bitboard

```python
subject = bc.me()

subject.attack_tiles_into(out)
```

### buffs

```python
def buffs(self) -> BuffCollection
```

Capture the unit's current buffs; raises Error if the unit is not visible.

Evaluate your champion's options during its turn.

```python
subject = bc.me()

result = subject.buffs()
```

### focus

```python
def focus(self) -> float
```

Return current focus; raises Error if the unit is not visible.

Evaluate your champion's options during its turn.

```python
subject = bc.me()

result = subject.focus()
```

### health

```python
def health(self) -> float
```

Return current health; raises Error if the unit is not visible.

Evaluate your champion's options during its turn.

```python
subject = bc.me()

result = subject.health()
```

### is_visible

```python
def is_visible(self) -> bool
```

Return whether the unit is currently visible.

Evaluate your champion's options during its turn.

```python
subject = bc.me()

is_visible = subject.is_visible()
```

### max_health

```python
def max_health(self) -> float
```

Return current maximum health; raises Error if the unit is not visible.

Evaluate your champion's options during its turn.

```python
subject = bc.me()

result = subject.max_health()
```

### position

```python
def position(self) -> Vec2
```

Return the current tile; raises Error if the unit is not visible.

Evaluate your champion's options during its turn.

```python
subject = bc.me()

result = subject.position()
```

### strength

```python
def strength(self) -> float
```

Return current strength; raises Error if the unit is not visible.

Evaluate your champion's options during its turn.

```python
subject = bc.me()

result = subject.strength()
```

## cambc.Vec2

### __add__

```python
def __add__(self, other: Vec2) -> Vec2
```



### __floordiv__

```python
def __floordiv__(self, n: int) -> Vec2
```



### __hash__

```python
def __hash__(self) -> int
```



### __init__

```python
def __init__(self, x: int, y: int) -> None
```



### __mul__

```python
def __mul__(self, n: int) -> Vec2
```



### __neg__

```python
def __neg__(self) -> Vec2
```



### __pos__

```python
def __pos__(self) -> Vec2
```



### __rmul__

```python
def __rmul__(self, n: int) -> Vec2
```



### __sub__

```python
def __sub__(self, other: Vec2) -> Vec2
```



### chebyshev_distance

```python
def chebyshev_distance(self, other: Vec2) -> int
```

Return the Chebyshev distance, the number of king moves between the tiles. Args: other: Other vector.

Compare positions or adjust a movement direction.

Inputs:
- other: Vec2

```python
subject = bc.Vec2(3, 4)

result = subject.chebyshev_distance(other)
```

### cross

```python
def cross(self, other: Vec2) -> int
```

Return the signed 2D cross product. Args: other: Other vector.

Compare positions or adjust a movement direction.

Inputs:
- other: Vec2

```python
subject = bc.Vec2(3, 4)

result = subject.cross(other)
```

### dot

```python
def dot(self, other: Vec2) -> int
```

Return the dot product. Args: other: Other vector.

Compare positions or adjust a movement direction.

Inputs:
- other: Vec2

```python
subject = bc.Vec2(3, 4)

result = subject.dot(other)
```

### length_squared

```python
def length_squared(self) -> int
```

Return the squared Euclidean length.

Compare positions or adjust a movement direction.

```python
subject = bc.Vec2(3, 4)

result = subject.length_squared()
```

### reflect_horizontal

```python
def reflect_horizontal(self) -> Vec2
```

Return this position reflected across the map horizontally, reversing x.

Compare positions or adjust a movement direction.

```python
subject = bc.Vec2(3, 4)

result = subject.reflect_horizontal()
```

### reflect_vertical

```python
def reflect_vertical(self) -> Vec2
```

Return this position reflected across the map vertically, reversing y.

Compare positions or adjust a movement direction.

```python
subject = bc.Vec2(3, 4)

result = subject.reflect_vertical()
```

### rotate_180

```python
def rotate_180(self) -> Vec2
```

Return this position rotated 180 degrees within the map.

Compare positions or adjust a movement direction.

```python
subject = bc.Vec2(3, 4)

result = subject.rotate_180()
```

### rotate_ccw

```python
def rotate_ccw(self) -> Vec2
```

Return this direction rotated 45 degrees counter-clockwise.

Compare positions or adjust a movement direction.

```python
subject = bc.Vec2(3, 4)

result = subject.rotate_ccw()
```

### rotate_cw

```python
def rotate_cw(self) -> Vec2
```

Return this direction rotated 45 degrees clockwise.

Compare positions or adjust a movement direction.

```python
subject = bc.Vec2(3, 4)

result = subject.rotate_cw()
```

### x

```python
def x(self) -> int
```

Horizontal coordinate or displacement.

### y

```python
def y(self) -> int
```

Vertical coordinate or displacement; +y is north.

## cambc.vision

### altar_lock_at

```python
def altar_lock_at(position: Vec2) -> AltarLock
```

The altar lock on a tile, ally first. Args: position: Tile to query.

Check visible objects before choosing a destination.

Inputs:
- position: Vec2

```python
result = bc.vision.altar_lock_at(position)
```

### altar_lock_tiles

```python
def altar_lock_tiles(team: Optional[Team] = None) -> Bitboard
```

Return the tiles of visible altar locks. Args: team: Team to include, or None for both teams.

Check visible objects before choosing a destination.

Inputs:
- team: Optional[Team]

```python
result = bc.vision.altar_lock_tiles(team)
```

### altar_lock_tiles_into

```python
def altar_lock_tiles_into(out: Bitboard, team: Optional[Team] = None) -> None
```

Like altar_lock_tiles, but writes into out. Args: out: Destination Bitboard; its previous contents are overwritten. team: Team to include, or None for both teams.

Check visible objects before choosing a destination.

Inputs:
- out: Bitboard
- team: Optional[Team]

```python
bc.vision.altar_lock_tiles_into(out, team)
```

### altar_locks

```python
def altar_locks(team: Optional[Team] = None) -> list[AltarLock]
```

Return snapshots of visible altar locks. Args: team: Team to include, or None for both teams.

Check visible objects before choosing a destination.

Inputs:
- team: Optional[Team]

```python
result = bc.vision.altar_locks(team)
```

### camp_at

```python
def camp_at(position: Vec2) -> Camp
```

Return the visible camp currently on a tile; raises Error if there is none or the tile is hidden. Args: position: Tile to query.

Check visible objects before choosing a destination.

Inputs:
- position: Vec2

```python
result = bc.vision.camp_at(position)
```

### camp_groups

```python
def camp_groups() -> list[_map.CampGroup]
```

Camp groups with at least one spawn tile in vision.

Check visible objects before choosing a destination.

```python
result = bc.vision.camp_groups()
```

### camp_tiles

```python
def camp_tiles() -> Bitboard
```

Return the tiles of visible camps.

Check visible objects before choosing a destination.

```python
result = bc.vision.camp_tiles()
```

### camp_tiles_into

```python
def camp_tiles_into(out: Bitboard) -> None
```

Like camp_tiles, but writes into out. Args: out: Destination Bitboard; its previous contents are overwritten.

Check visible objects before choosing a destination.

Inputs:
- out: Bitboard

```python
bc.vision.camp_tiles_into(out)
```

### camps

```python
def camps() -> list[Camp]
```

Return the visible camps.

Check visible objects before choosing a destination.

```python
result = bc.vision.camps()
```

### champion_at

```python
def champion_at(position: Vec2) -> Champion
```

Return the visible champion on a tile; raises Error if there is none or the tile is hidden. Args: position: Tile to query.

Check visible objects before choosing a destination.

Inputs:
- position: Vec2

```python
result = bc.vision.champion_at(position)
```

### champion_tiles

```python
def champion_tiles(team: Optional[Team] = None) -> Bitboard
```

Visible champions of a team, or of both teams. Args: team: Team to include, or None for both teams.

Check visible objects before choosing a destination.

Inputs:
- team: Optional[Team]

```python
result = bc.vision.champion_tiles(team)
```

### champion_tiles_into

```python
def champion_tiles_into(out: Bitboard, team: Optional[Team] = None) -> None
```

Like champion_tiles, but writes into out. Args: out: Destination Bitboard; its previous contents are overwritten. team: Team to include, or None for both teams.

Check visible objects before choosing a destination.

Inputs:
- out: Bitboard
- team: Optional[Team]

```python
bc.vision.champion_tiles_into(out, team)
```

### champions

```python
def champions(team: Optional[Team] = None) -> list[Champion]
```

Return the visible champions. Args: team: Team to include, or None for both teams.

Check visible objects before choosing a destination.

Inputs:
- team: Optional[Team]

```python
result = bc.vision.champions(team)
```

### has_altar_lock

```python
def has_altar_lock(position: Vec2) -> bool
```

Return whether a visible altar lock of either team is on a tile. Args: position: Tile to query.

Check visible objects before choosing a destination.

Inputs:
- position: Vec2

```python
has_altar_lock = bc.vision.has_altar_lock(position)
```

### has_camp

```python
def has_camp(position: Vec2) -> bool
```

Return whether a visible camp is on a tile. Args: position: Tile to query.

Check visible objects before choosing a destination.

Inputs:
- position: Vec2

```python
has_camp = bc.vision.has_camp(position)
```

### has_champion

```python
def has_champion(position: Vec2) -> bool
```

Return whether a visible champion is on a tile. Args: position: Tile to query.

Check visible objects before choosing a destination.

Inputs:
- position: Vec2

```python
has_champion = bc.vision.has_champion(position)
```

### has_teleport

```python
def has_teleport(position: Vec2) -> bool
```

Return whether a visible teleport reservation is on a tile. Args: position: Tile to query.

Check visible objects before choosing a destination.

Inputs:
- position: Vec2

```python
has_teleport = bc.vision.has_teleport(position)
```

### has_ward

```python
def has_ward(position: Vec2, team: Optional[Team] = None) -> bool
```

Return whether a visible ward is on a tile; hidden wards return False. Args: position: Tile to query. team: Team to restrict to, or None for either team.

Check visible objects before choosing a destination.

Inputs:
- position: Vec2
- team: Optional[Team]

```python
has_ward = bc.vision.has_ward(position, team)
```

### teleport_at

```python
def teleport_at(position: Vec2) -> Teleport
```

The teleport reservation on a tile. Args: position: Tile to query.

Check visible objects before choosing a destination.

Inputs:
- position: Vec2

```python
result = bc.vision.teleport_at(position)
```

### teleport_tiles

```python
def teleport_tiles() -> Bitboard
```

Return the tiles of visible teleport reservations.

Check visible objects before choosing a destination.

```python
result = bc.vision.teleport_tiles()
```

### teleport_tiles_into

```python
def teleport_tiles_into(out: Bitboard) -> None
```

Like teleport_tiles, but writes into out. Args: out: Destination Bitboard; its previous contents are overwritten.

Check visible objects before choosing a destination.

Inputs:
- out: Bitboard

```python
bc.vision.teleport_tiles_into(out)
```

### teleports

```python
def teleports() -> list[Teleport]
```

Return snapshots of visible teleport reservations.

Check visible objects before choosing a destination.

```python
result = bc.vision.teleports()
```

### visible_tiles

```python
def visible_tiles() -> Bitboard
```

Return every tile visible to the bot's champion.

Check visible objects before choosing a destination.

```python
result = bc.vision.visible_tiles()
```

### visible_tiles_into

```python
def visible_tiles_into(out: Bitboard) -> None
```

Like visible_tiles, but writes into out. Args: out: Destination Bitboard; its previous contents are overwritten.

Check visible objects before choosing a destination.

Inputs:
- out: Bitboard

```python
bc.vision.visible_tiles_into(out)
```

### ward_at

```python
def ward_at(position: Vec2, team: Optional[Team] = None) -> Ward
```

Snapshot of the ward on a tile, optionally of one team. Args: position: Tile to query. team: Team to restrict to, or None for either team.

Check visible objects before choosing a destination.

Inputs:
- position: Vec2
- team: Optional[Team]

```python
result = bc.vision.ward_at(position, team)
```

### ward_tiles

```python
def ward_tiles(team: Optional[Team] = None) -> Bitboard
```

Return the tiles of visible wards. Args: team: Team to include, or None for both teams.

Check visible objects before choosing a destination.

Inputs:
- team: Optional[Team]

```python
result = bc.vision.ward_tiles(team)
```

### ward_tiles_into

```python
def ward_tiles_into(out: Bitboard, team: Optional[Team] = None) -> None
```

Like ward_tiles, but writes into out. Args: out: Destination Bitboard; its previous contents are overwritten. team: Team to include, or None for both teams.

Check visible objects before choosing a destination.

Inputs:
- out: Bitboard
- team: Optional[Team]

```python
bc.vision.ward_tiles_into(out, team)
```

### wards

```python
def wards(team: Optional[Team] = None) -> list[Ward]
```

Snapshots of visible wards, optionally of one team. Args: team: Team to include, or None for both teams.

Check visible objects before choosing a destination.

Inputs:
- team: Optional[Team]

```python
result = bc.vision.wards(team)
```

## cambc.Ward

### is_ally

```python
def is_ally(self) -> bool
```

Check whether this ward belongs to the observing team.

Check visible objects before choosing a destination.

Inputs:
- subject: bc.Ward (a valid instance)

```python
is_ally = subject.is_ally()
```

### is_enemy

```python
def is_enemy(self) -> bool
```

Check whether this ward belongs to the opposing team.

Check visible objects before choosing a destination.

Inputs:
- subject: bc.Ward (a valid instance)

```python
is_enemy = subject.is_enemy()
```

### position

```python
def position(self) -> Vec2
```

Return the ward's tile.

Check visible objects before choosing a destination.

Inputs:
- subject: bc.Ward (a valid instance)

```python
result = subject.position()
```

### remaining_time

```python
def remaining_time(self) -> Optional[int]
```

Return the rounds before the ward expires, or None if it does not expire.

Check visible objects before choosing a destination.

Inputs:
- subject: bc.Ward (a valid instance)

```python
result = subject.remaining_time()
```

### team

```python
def team(self) -> Team
```

Return the team that owns the ward.

Check visible objects before choosing a destination.

Inputs:
- subject: bc.Ward (a valid instance)

```python
result = subject.team()
```

### visible_tiles

```python
def visible_tiles(self) -> Bitboard
```

Return the tiles this ward sees.

Check visible objects before choosing a destination.

Inputs:
- subject: bc.Ward (a valid instance)

```python
result = subject.visible_tiles()
```

### visible_tiles_from

```python
def visible_tiles_from(position: Vec2) -> Bitboard
```

Return the vision a ward would have at a tile. Args: position: Hypothetical ward tile.

Check visible objects before choosing a destination.

Inputs:
- position: Vec2

```python
result = bc.Ward.visible_tiles_from(position)
```

### visible_tiles_from_into

```python
def visible_tiles_from_into(position: Vec2, out: Bitboard) -> None
```

Like visible_tiles_from, but writes into out. Args: position: Hypothetical ward tile. out: Destination Bitboard; its previous contents are overwritten.

Check visible objects before choosing a destination.

Inputs:
- position: Vec2
- out: Bitboard

```python
bc.Ward.visible_tiles_from_into(position, out)
```

### visible_tiles_into

```python
def visible_tiles_into(self, out: Bitboard) -> None
```

Like visible_tiles, but writes into out. Args: out: Destination Bitboard; its previous contents are overwritten.

Check visible objects before choosing a destination.

Inputs:
- subject: bc.Ward (a valid instance)
- out: Bitboard

```python
subject.visible_tiles_into(out)
```
